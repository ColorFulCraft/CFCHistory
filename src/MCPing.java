import java.io.*;
import java.net.*;
import java.text.SimpleDateFormat;
import java.util.Date;

public class MCPing {
    
    public static void main(String[] args) {
        String host = "mc.cfcmc.cc";
        int port = 25565;
        String outputPath = args.length > 0 ? args[0] : "server.json";
        
        ServerInfo info = pingServer(host, port);
        saveToJson(info, outputPath);
    }
    
    public static ServerInfo pingServer(String host, int port) {
        ServerInfo info = new ServerInfo();
        info.host = host;
        info.port = port;
        info.timestamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());
        
        try {
            Socket socket = new Socket();
            socket.connect(new InetSocketAddress(host, port), 10000);
            
            DataInputStream in = new DataInputStream(socket.getInputStream());
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            
            // 发送握手包
            ByteArrayOutputStream handshake = new ByteArrayOutputStream();
            DataOutputStream handshakeOut = new DataOutputStream(handshake);
            
            handshakeOut.writeByte(0x00);
            writeVarInt(handshakeOut, -1);
            writeString(handshakeOut, host);
            handshakeOut.writeShort(port);
            writeVarInt(handshakeOut, 1);
            
            writeVarInt(out, handshake.size());
            out.write(handshake.toByteArray());
            
            // 发送状态请求
            out.writeByte(0x01);
            out.writeByte(0x00);
            
            // 接收响应
            int length = readVarInt(in);
            int packetId = readVarInt(in);
            
            if (packetId == 0x00) {
                String jsonResponse = readString(in);
                parseServerInfo(info, jsonResponse);
                info.online = true;
            }
            
            socket.close();
            
        } catch (ConnectException | SocketTimeoutException e) {
            info.online = false;
            info.error = "连接超时或服务器离线";
        } catch (IOException e) {
            info.online = false;
            info.error = e.getMessage();
        }
        
        return info;
    }
    
    private static void parseServerInfo(ServerInfo info, String json) {
        try {
            // 简化解析，实际可用JSON库
            info.rawResponse = json;
            
            // 提取描述
            int descIndex = json.indexOf("\"description\":");
            if (descIndex != -1) {
                int textIndex = json.indexOf("\"text\":", descIndex);
                if (textIndex != -1) {
                    int start = json.indexOf("\"", textIndex + 6) + 1;
                    int end = json.indexOf("\"", start);
                    if (end > start) {
                        info.description = json.substring(start, end);
                    }
                }
            }
            
            // 提取玩家信息
            int playersIndex = json.indexOf("\"players\":");
            if (playersIndex != -1) {
                int maxStart = json.indexOf("\"max\":", playersIndex) + 6;
                int maxEnd = findEnd(json, maxStart);
                int onlineStart = json.indexOf("\"online\":", playersIndex) + 9;
                int onlineEnd = findEnd(json, onlineStart);
                
                if (maxEnd > maxStart && onlineEnd > onlineStart) {
                    info.maxPlayers = Integer.parseInt(json.substring(maxStart, maxEnd).trim());
                    info.onlinePlayers = Integer.parseInt(json.substring(onlineStart, onlineEnd).trim());
                }
            }
            
            // 提取版本
            int versionIndex = json.indexOf("\"version\":");
            if (versionIndex != -1) {
                int nameStart = json.indexOf("\"name\":", versionIndex) + 7;
                int nameEnd = json.indexOf("\"", nameStart);
                if (nameEnd > nameStart) {
                    info.version = json.substring(nameStart, nameEnd);
                }
            }
            
        } catch (Exception e) {
            info.error = "解析失败: " + e.getMessage();
        }
    }
    
    private static int findEnd(String str, int start) {
        for (int i = start; i < str.length(); i++) {
            char c = str.charAt(i);
            if (c == ',' || c == '}' || c == ']') {
                return i;
            }
        }
        return str.length();
    }
    
    public static void saveToJson(ServerInfo info, String filePath) {
        try (PrintWriter writer = new PrintWriter(filePath)) {
            writer.println("{");
            writer.println("  \"host\": \"" + escapeJson(info.host) + "\",");
            writer.println("  \"port\": " + info.port + ",");
            writer.println("  \"online\": " + info.online + ",");
            writer.println("  \"timestamp\": \"" + info.timestamp + "\",");
            writer.println("  \"version\": \"" + escapeJson(info.version) + "\",");
            writer.println("  \"description\": \"" + escapeJson(info.description) + "\",");
            writer.println("  \"onlinePlayers\": " + info.onlinePlayers + ",");
            writer.println("  \"maxPlayers\": " + info.maxPlayers + ",");
            writer.println("  \"error\": " + (info.error != null ? "\"" + escapeJson(info.error) + "\"" : "null"));
            writer.println("}");
        } catch (IOException e) {
            System.err.println("保存JSON失败: " + e.getMessage());
        }
    }
    
    private static String escapeJson(String str) {
        if (str == null) return "";
        return str.replace("\\", "\\\\")
                  .replace("\"", "\\\"")
                  .replace("\n", "\\n")
                  .replace("\r", "\\r")
                  .replace("\t", "\\t");
    }
    
    // VarInt 编解码方法
    private static void writeVarInt(DataOutputStream out, int value) throws IOException {
        while (true) {
            if ((value & 0xFFFFFF80) == 0) {
                out.writeByte(value);
                return;
            }
            out.writeByte(value & 0x7F | 0x80);
            value >>>= 7;
        }
    }
    
    private static int readVarInt(DataInputStream in) throws IOException {
        int value = 0;
        int size = 0;
        int b;
        while (((b = in.readByte()) & 0x80) == 0x80) {
            value |= (b & 0x7F) << (size++ * 7);
            if (size > 5) throw new IOException("VarInt too long");
        }
        return value | ((b & 0x7F) << (size * 7));
    }
    
    private static void writeString(DataOutputStream out, String str) throws IOException {
        byte[] bytes = str.getBytes("UTF-8");
        writeVarInt(out, bytes.length);
        out.write(bytes);
    }
    
    private static String readString(DataInputStream in) throws IOException {
        int length = readVarInt(in);
        byte[] bytes = new byte[length];
        in.readFully(bytes);
        return new String(bytes, "UTF-8");
    }
    
    static class ServerInfo {
        String host;
        int port = 25565;
        boolean online = false;
        String timestamp;
        String version = "";
        String description = "";
        int onlinePlayers = 0;
        int maxPlayers = 0;
        String error = null;
        String rawResponse = "";
    }
}

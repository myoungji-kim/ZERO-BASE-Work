import java.io.*;

public class Work01 {
    public static void main(String[] args) {
        try {
            File file = new File("index.html"); // 상대 경로로 파일 생성
            BufferedWriter writer = new BufferedWriter(new FileWriter(file));
            writer.write("<html>" +
                    "<head>" +
                    "<meta charset='UTF-8'>" +
                    "<style>" +
                    "table { border-collapse: collapse; width: 100%; }" +
                    "th, td { border:solid 1px #000; }" +
                    "</style>" +
                    "</head>" +
                    "<body>" +
                    "<h1>자바 환경정보</h1>" +
                    "<table>" +
                        "<tr style='text-align:center;'><th>키</th><th></th></tr>");
            for (Object k : System.getProperties().keySet()) {
                String key = k.toString();
                String value = System.getProperty(key);
                writer.write("<tr>" +
                                    "<td>"+key+"</td>" +
                                    "<td>"+value+"</td>" +
                                "</tr>");
            }
            writer.write("</tbody>" +
                    "</table>" +
                    "</body>" +
                    "</html>");
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

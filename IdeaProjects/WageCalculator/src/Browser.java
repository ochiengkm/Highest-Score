public class Browser {
    public void navigate(){
        String ip = findIpAddress();
        String html = sendHttpRequest(ip);
        System.out.println(html);

    }

    private String findIpAddress() {
        return "127.0.0.1";
    }

    private String sendHttpRequest(String ip) {
        return "<html>Hello World</html>";
    }


}

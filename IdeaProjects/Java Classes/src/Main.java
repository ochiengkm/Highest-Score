public class Main {
    public static void main(String[] args) {
        var textBox1 = new TextBox();
        var textBox2 = new TextBox();
        textBox1.setText("This is Box 1");
        textBox2.setText("This is Box 2");
        textBox1.clear();
        System.out.println(textBox1.text);
        System.out.println(textBox2.text);

    }
}
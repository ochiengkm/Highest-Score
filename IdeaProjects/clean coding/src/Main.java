public class Main {
    public static void main(String[] args) {
        int[][] myNumbers = {{242, 34, 33, 63, 28}, {39, 21, 9, 86}};
        for (int i = 0; i < myNumbers.length; i++){
            for (int j = 0; j < myNumbers[i].length; j++){
                System.out.println(myNumbers[i][j]);
            }
        }
        System.out.println(greetWithName(" Jane ", "Doe"));

    }
    public static String greetWithName(String name,String name2){

        return "Hello".concat(name).concat(name2);
    }
}
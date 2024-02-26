import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        System.out.print("Enter username to log in: ");
        Scanner scanner = new Scanner(System.in);

        String role = scanner.next().toLowerCase();
        scanner.nextLine();
        switch (role) {
            case "admin":
                System.out.print("Enter Admin Password: ");
                String adminPass = scanner.nextLine();
                if (adminPass.equals("Hello/2024"))
                    System.out.println("Access Granted");
                else
                    System.out.println("Incorrect Password.\nAccess Denied");
                break;
            case "moderator":
                System.out.print("Enter moderator password: ");
                String moderatorPass = scanner.next();
                if (moderatorPass.equals("Welcome/2024"))
                    System.out.println("Access Granted");
                else
                    System.out.println("Incorrect Password.\nAccess Denied...");
                break;
            default:
                System.out.println("You are guest");
        }
        }

    }


import java.text.NumberFormat;
import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        int principal = 0;
        double rate = 0;
        int period = 0;
        principal = (int) readNumber("Enter principal in KES: ", 1000, 2_000_000);
        rate = readNumber("Enter interest rate: ", 1, 30);
        period = (int) readNumber("Enter period in years: ", 1, 30);
        NumberFormat currency = NumberFormat.getCurrencyInstance();
        printMortgage(currency, principal, rate, period);

        printPaymentSchedule(period, principal, rate, currency);

    }

    private static void printMortgage(NumberFormat currency, int principal, double rate, int period) {
        String mortgage = currency.format(calculateMortgage(principal, rate, period));
        System.out.println("Monthly payments: ".concat(mortgage));
        System.out.println("MORTGAGE");
    }

    private static void printPaymentSchedule(int period, int principal, double rate, NumberFormat currency) {
        System.out.println("Payment Schedule;");
        System.out.println("_________________");
        for (int month = 1; month <= period * 12; month++){
            double balance = getBalance(principal, rate, period, month);
            System.out.println(currency.format(balance));
        }
    }

    public static double getBalance(int principal, double rate, int period,
                                    int numberOfPaymentsMade) {
        double monthlyInterest = (rate / 12) / 100;
        int numberOfPayments = period * 12;

        double remainingBalance = principal * (Math.pow((1 + monthlyInterest), numberOfPayments) - Math.pow((1 + monthlyInterest), numberOfPaymentsMade))
                / (Math.pow((1 + monthlyInterest), numberOfPayments) - 1);
        return remainingBalance;
    }
    public static double calculateMortgage(int principal, double rate, int period) {
        double monthlyInterest = (rate / 12) / 100;
        int numberOfPayments = period * 12;
        return principal * (monthlyInterest * Math.pow((1 + monthlyInterest), numberOfPayments)) / (Math.pow((1 + monthlyInterest), numberOfPayments) - 1);
    }
    public static double readNumber(String prompt, double min, double max) {
        double value;
        Scanner scanner = new Scanner(System.in);
        do {
            System.out.print(prompt);
            value = scanner.nextDouble();
            if (value >= min && value <= max) {
                break;
            } else {
                System.out.println("Enter a value between " + min + " and " + max);
            }
        }
        while (true);
        return value;
    }


    }

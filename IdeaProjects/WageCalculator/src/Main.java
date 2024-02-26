public class Main {
    public static void main(String[] args) {
        var employee = new Employee(50000, 250);
        int wage = employee.calculateWage();
        System.out.println(wage);
        Employee.printNumberOfEmployees();
    }
}
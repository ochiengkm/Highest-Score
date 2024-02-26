public class Employee {
    private int baseSalary;
    private int hourlyRate;
    private static int numberOfEmployees;

    public Employee(int baseSalary, int hourlyRate){
        setBaseSalary(baseSalary);
        setHourlyRate(hourlyRate);
        numberOfEmployees++;
    }
    public static void printNumberOfEmployees(){
        System.out.println(numberOfEmployees);
    }

    public int calculateWage(int extraHours) {

        return getBaseSalary() + (getHourlyRate() * extraHours);
    }public int calculateWage() {

        return calculateWage(27);
    }

    private int getBaseSalary() {
        return baseSalary;
    }

    private void setBaseSalary(int baseSalary) {
        if (baseSalary <= 0)
            throw new IllegalArgumentException("Base salary cannot be zero or less");
        this.baseSalary = baseSalary;
    }

    private int getHourlyRate() {
        return hourlyRate;
    }

    private void setHourlyRate(int hourlyRate) {
        if (hourlyRate <= 0)
            throw new IllegalArgumentException("Hourly rate cannot be zero or less");
        this.hourlyRate = hourlyRate;
    }
}

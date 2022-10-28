package PythonWorkshop.Examples;

// Commenting

class Basics {
    public static void main(String[] args) {
        String sep = "";
        for (int i = 0; i < 10; i++)
            sep += "=";

        // Println

        System.out.println(sep + 0 + sep);

        System.out.println("Hello World");

        // Print

        System.out.println(sep + 1 + sep);

        System.out.print("Hello");
        System.out.println("World");

        // Division

        System.out.println(sep + 5 + sep);

        System.out.println(5 / 2);

        System.out.println(5 % 2);

        System.out.println(5.0 / 2.0);

        // Boolean types

        System.out.println(sep + 6 + sep);

        System.out.println(true);
        System.out.println(false);

        // Boolean statements

        System.out.println(sep + 7 + sep);

        System.out.println(true && true);
        System.out.println(true && false);
        System.out.println(false && false);

        System.out.println(true || true);
        System.out.println(true || false);
        System.out.println(false || false);

        System.out.println(!true);
        System.out.println(!false);

    }
}
package GetTrainTestDataSet;
/**
 * This script will separate the patient list into 2 distinguished files: a list of recovered patients and a list
 *  of patients under treatment, respectively named df_train and df_test as they serve the purpose of training
 *  and testing data in machine learning.
 *
 * @author Tuan Khoi Nguyen (tuankhoin@student.unimelb.edu.au)
 */

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

/**
 * Function class to execute
 */
public class getTrainTest {

    static ArrayList<String[]> data = new ArrayList<String[]>();

    /**
     * Note: Please modify the file path if you are going to use the script. Example: "[path]\\df_total.csv"
     * @param args  System argument
     */
    public static void main(String[] args) {
        System.out.println("Training & Testing Dataset Generator");
        System.out.println("By Tuan Khoi Nguyen\n");
        System.out.println("Enter directory to \"df_total.csv\" (Example: C:\\ContainFolder\\ ): ");
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        System.out.println("Enter directory to export \"df_train.csv\" and \"df_test.csv\" (Example: C:\\ContainFolder\\ ): ");
        scanner = new Scanner(System.in);
        String output = scanner.nextLine();
        int nline = read(input.replace("\\","\\\\")+"df_total.csv");
        write(output.replace("\\","\\\\") + "df_test.csv", nline, false);
        write(output.replace("\\","\\\\") + "df_train.csv", nline, true);
    }

    /**
     * Read df_total into an array list of lines
     * @param filename  The input file
     * @return          The number of lines read
     */
    public static int read(String filename) {
        int nline = 0;
        try (BufferedReader br =
                     new BufferedReader(new FileReader(filename))) {
            String text;

            while ((text = br.readLine()) != null) {
                // Put each line of data into an array
                String[] dataLine = text.split(",");
                data.add(dataLine);
                nline++;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return nline;
    }

    /**
     * Write the new files from the processed list of read() function
     * @param s         Operation argument
     * @param nline     Number of lines read, retrieved from read()
     * @param isTrain   If true, it will pick recovered patients to make df_train.
     *                  If false, it will pick patients under treatment to make df_test
     */
    public static void write(String s, int nline, boolean isTrain) {
        try (PrintWriter pw =
                     new PrintWriter(new FileWriter(s))) {
            // Printing variable names
            writeLine(pw, data.get(0));

            for (int i = 1; i < nline; i++) {
                // A patient under treatment will not have full number of information vars, lacking of days hospitalized
                if ((data.get(i).length == data.get(0).length && isTrain) ||
                        (data.get(i).length != data.get(0).length && !isTrain)) {
                    writeLine(pw, data.get(i));
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Print a new line to the written file
     * @param pw        PrintWriter operation
     * @param dataLine  The line being printed
     */
    public static void writeLine(PrintWriter pw, String[] dataLine){
        boolean isFirst=true;
        for (String str:dataLine){
            // If processing first variable of line, don't add "," before it
            if (isFirst){
                isFirst=false;
            }
            else {
                pw.format(",");
            }
            pw.format(str);
        }
        pw.format("\n");
    }
}

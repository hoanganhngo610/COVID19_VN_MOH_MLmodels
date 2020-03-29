import java.io.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class DataConversion {
    static ArrayList<String[]> data = new ArrayList<String[]>();
    public static void main(String[] args) {
        int nline=read("C:\\Users\\HP OMEN 15\\Desktop\\Workspace\\boyte\\src\\main\\java\\table\\modifiedSource.csv");
        write("C:\\Users\\HP OMEN 15\\Desktop\\Workspace\\boyte\\src\\main\\java\\table\\process_table.csv",nline);
    }


    public static int read(String filename) {
        int nline = 0;
        try (BufferedReader br =
                     new BufferedReader(new FileReader(filename))) {
            String text;

            while ((text = br.readLine()) != null) {
                // code goes here
                String[] dataLine = text.split(",");
                data.add(dataLine);
                nline++;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return nline;
    }

    public static void write(String s, int nline){
        try (PrintWriter pw =
                     new PrintWriter(new FileWriter(s))) {
            //code goes here
            pw.write("STT,Age,isMale,ORIGIN_EUROPE,ORIGIN_CHINA,ORIGIN_US,ORIGIN_DOMESTIC," +
                    "symptomsToHospitalization,ONSET_FEVER,ONSET_COUGH,ONSET_TIRED,ONSET_THROAT,ONSET_RES," +
                    "MedicalHistory,Hospital,LOS\n");
            for(int i=1;i<nline;i++){
                pw.format(data.get(i)[0]+",");
                pw.format(data.get(i)[1]+",");

                if (data.get(i)[2].equals("Nam")){
                    pw.format("1" + ",,,,,");
                } else {
                    pw.format("0" + ",,,,,");
                }

                if (data.get(i)[3].equals("N/A")){
                    pw.format("N/A,,,,,,,");
                } else {
                    int days = dayOfYear(data.get(i)[4]) - dayOfYear(data.get(i)[3]);
                    pw.format(days + ",,,,,,,");
                }

                boolean isHos = false;
                String[] legal = {"ch? r?y","?ông anh","b?ch mai","nhi trung ??ng",
                        "trung ??ng hu?","nhi?t ??i tp", "nhi ??ng"};
                for (String word:legal) {
                    if (data.get(i)[5].toLowerCase().contains(word)) {
                        isHos=true;
                        break;
                    }
                }
                if (isHos){
                    pw.format("1,");
                } else {
                    pw.format("0,");
                }

                if (data.get(i)[6].equals("N/A")){
                    pw.format("N/A");
                } else {
                    int hospitalDays = dayOfYear(data.get(i)[6]) - dayOfYear(data.get(i)[4]);
                    pw.format(String.valueOf(hospitalDays));
                }
                pw.write("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static int dayOfYear(String date){
        String[] element=date.split("/");
        switch(element[0]){
            case "1":
            case "01":
                return Integer.parseInt(element[1]);
            case "2":
            case "02":
                return 31+Integer.parseInt(element[1]);
            case "3":
            case "03":
                return 31+29+Integer.parseInt(element[1]);
            case "4":
            case "04":
                return 31+29+31+Integer.parseInt(element[1]);
            default:
                return 0;
        }
    }
}
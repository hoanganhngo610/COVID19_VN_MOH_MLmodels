/**
* This script is to process the raw cleaned datafile, and process them to
* export a complete processed datafile to serve prediction modelling.
* @author Tuan Khoi Nguyen (tuankhoin@student.unimelb.edu.au)
*/

import java.io.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

/**
* This will read the cleaned original datafile modifiedSource.csv, then output
* process_table.csv as the processed data with a few informations added
*/
public class DataConversion {
    static ArrayList<String[]> data = new ArrayList<String[]>();
    public static void main(String[] args) {
      // If you plan to use this file, make sure to modify the file paths first
        int nline=read("\\table\\modifiedSource.csv");
        write("\\table\\process_table.csv",nline);
    }

/**
* Reader function that will process the original data
*/
    public static int read(String filename) {
        int nline = 0;
        try (BufferedReader br =
                     new BufferedReader(new FileReader(filename))) {
            String text;

            while ((text = br.readLine()) != null) {
                /**
                *   Each line will be split into an array of datas
                *   Array order: STT, Tuoi, Nam/Nu, ngayKhoiPhat, ngayDuongTinh,
                *   bvDieuTri, ngayXuatVien
                */
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
    * Process function that will parse the raw data into a new file
    */
    public static void write(String s, int nline){
        try (PrintWriter pw =
                     new PrintWriter(new FileWriter(s))) {
            //Column printing
            pw.write("STT,Age,isMale,ORIGIN_EUROPE,ORIGIN_CHINA,ORIGIN_US,ORIGIN_DOMESTIC,ORIGIN_ASEAN," +
                    "symptomsToHospitalization,ONSET_FEVER,ONSET_COUGH,ONSET_TIRED,ONSET_THROAT,ONSET_RES," +
                    "MedicalHistory,Hospital,LOS\n");
            for(int i=1;i<nline;i++){
                // STT, Tuoi
                pw.format(data.get(i)[0]+",");
                pw.format(data.get(i)[1]+",");

                // Nam=1;Nu=0
                if (data.get(i)[2].equals("Nam")){
                    pw.format("1" + ",,,,,,");
                } else {
                    pw.format("0" + ",,,,,,");
                }

                /**
                * If ngayKhoiPhat exists, we will retrieve the number of days
                * being infected without being treated, that is
                * ngayDuongTinh - ngayKhoiPhat
                */
                if (data.get(i)[3].equals("N/A")){
                    pw.format("N/A,,,,,,,");
                } else {
                    int days = dayOfYear(data.get(i)[4]) - dayOfYear(data.get(i)[3]);
                    pw.format(days + ",,,,,,,");
                }

                /**
                * Process keywords to check if the treatment hospital is from
                * the Central Government (BenhVienTrungUong)
                * 1=BenhVienTrungUong;0=BenhVienDiaPhuong
                */
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

                /**
                * If ngayXuatVien exists, we will retrieve the number of days
                * being treated, that is
                * ngayXuatVien - ngayDuongTinh
                */
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

    /**
    * This function will calculate to find out what day of year is the
    * argument date. For example, 1/2/2020 will be the 32nd day of year 2020.
    * Function is simplied to serve the current datafile.
    */
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

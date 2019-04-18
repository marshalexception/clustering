

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FileReader {
    String name, regex;
    FileReader (String name, String regex) {
        this.name = name;
        this.regex = regex;
    }

    public double[][] readFile() {
        List<double[]> lines = new ArrayList<>();
        FileInputStream fis = null;
        String line = "";
        DataInputStream myInput = null;
        try {
            fis = new FileInputStream(name);
            myInput = new DataInputStream(fis);
            while ((line = myInput.readLine()) != null) {
                String[] tmp = line.split(regex);
                double[] current = new double[tmp.length];
                for (int i = 0; i < tmp.length; i++) {
                    current[i] = Double.parseDouble(tmp[i]);
                }
                lines.add(current);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (myInput != null) {
                try {
                    myInput.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                System.out.println("Datei aus " + name + " erfolgreich eingelesen.");
            }
        }
        double[][] output = new double[lines.size()][0];
        lines.toArray(output);
        return output;
    }

    public void writeToFile (String path, double[][] matrix) {
        StringBuilder builder = new StringBuilder();
        try (PrintWriter writer = new PrintWriter(path)) {
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix.length; j++) {
                    if (j == matrix.length -1) {
                        builder.append(matrix[i][j] +"\n");
                    } else {
                        builder.append(matrix[i][j] + ";");
                    }
                }
            }
            writer.write(builder.toString());
        } catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getRegex() {
        return regex;
    }

    public void setRegex(String regex) {
        this.regex = regex;
    }
}

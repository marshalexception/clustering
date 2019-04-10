public class Main {

    public static void main(String[] args) {
        String name = "tmp.csv";
        String path = "data/" + name;
        String regex = ";";
        FileReader f = new FileReader(path, regex);

        System.out.println("Ähnlichkeitsmatrix: ");
        double[][] similarity_matrix = f.readFile();
        printMatrix(similarity_matrix);
        System.out.println("Distanzmatrix: ");
        double[][] distance_matrix = similarityToDistanceMatrix(similarity_matrix);
        printMatrix(distance_matrix);

        Symmetrization cur = Symmetrization.AVG;
        //System.out.println("symmetrisierte Distanzmatrix (" + cur + "):");
        double[][] symmetrized = symmetrize(distance_matrix, cur);
        //printMatrix(symmetrized);

        String newPath = "data/symmetrized/avg_symmetrized_" + name;
        System.out.println("symmetrisierte Distanzmatrix in Datei " + newPath + " geschrieben");
        f.writeToFile(newPath, symmetrized);
    }

    private static void printMatrix (double[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            System.out.print("|");
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(matrix[i][j] +"|");
            }
            System.out.println();
        }
    }

    private static double[][] similarityToDistanceMatrix (double[][] similarity_matrix) {
        double[][] distance_matrix = new double[similarity_matrix.length][similarity_matrix.length];
        for (int i = 0; i < distance_matrix.length; i++) {
            for (int j = 0; j < distance_matrix.length; j++) {
                distance_matrix[i][j] = 1 - similarity_matrix[i][j];
            }
        }
        return distance_matrix;
    }

    private static double[][] symmetrize (double[][] similarities, Symmetrization sym) {
        double[][] result = new double[similarities.length][similarities.length];
        for (int i = 0; i < similarities.length; i++) {
            for (int j = 0; j < similarities.length; j++) {
                double sim = 0;
                //keine Diagonale
                if (i != j) {
                    if (sym.equals(Symmetrization.AVG)) {
                        sim = (similarities[i][j] + similarities[j][i]) / 2;
                    } else if (sym.equals(Symmetrization.MIN)) {
                        sim = findMin(similarities[i][j], similarities[j][i]);
                    } else if (sym.equals(Symmetrization.MAX)) {
                        sim = findMax(similarities[i][j], similarities[j][i]);
                    }
                }
                result[i][j] = sim;
            }
        }
        return result;
    }

    private static double findMin(double a, double b) {
        if (a < b) {
            return a;
        } else {
            return b;
        }
    }

    private static double findMax(double a, double b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }
}

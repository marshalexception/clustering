package src;

public class Main {
    /**
     * Main-Methode um Umwandlung von Ähnlichkeits- zu Distanzmatrix vorzunehmen
     * @param args
     */
    public static void main(String[] args) {
        String name = "matrix_lenz.csv";
        String path = "data/lenz/" + name;
        String regex = ";";
        FileReader f = new FileReader(path, regex);

        System.out.println("Ähnlichkeitsmatrix: ");
        double[][] similarity_matrix = f.readFile();
        printMatrix(similarity_matrix);
        System.out.println("Distanzmatrix: ");
        double[][] distance_matrix = similarityToDistanceMatrix(similarity_matrix);
        printMatrix(distance_matrix);

        Symmetrization cur = Symmetrization.MAX;
        //System.out.println("symmetrisierte Distanzmatrix (" + cur + "):");
        double[][] symmetrized = symmetrize(similarity_matrix, cur);
        //printMatrix(symmetrized);

        String newPath = "data/max_symmetrized_" + name;
        System.out.println("symmetrisierte Distanzmatrix in Datei " + newPath + " geschrieben");
        f.writeToFile(newPath, symmetrized);
    }

    /**
     * Methode, um Matrix über Konsole sichtbar zu machen
     *
     * @param matrix Matrix die ausgegeben werden soll
     */
    private static void printMatrix (double[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            System.out.print("|");
            for (int j = 0; j < matrix.length; j++) {
                System.out.print(matrix[i][j] +"|");
            }
            System.out.println();
        }
    }

    /**
     * Wandelt die Input Ähnlichkeitsmatrix in eine Distanzmatrix (alle Werte -1) als Output
     *
     * @param similarity_matrix Ähnlichkeitsmatrix
     * @return Distanzmatrix
     */
    private static double[][] similarityToDistanceMatrix (double[][] similarity_matrix) {
        double[][] distance_matrix = new double[similarity_matrix.length][similarity_matrix.length];
        for (int i = 0; i < distance_matrix.length; i++) {
            for (int j = 0; j < distance_matrix.length; j++) {
                distance_matrix[i][j] = 1 - similarity_matrix[i][j];
            }
        }
        return distance_matrix;
    }

    /**
     * Symmetrisiert Distanzmatrix nach angegebener Strategie
     * @param similarities Distanzmatrix, die symmetrisiert werden soll
     * @param sym Symmetrisierungsstrategie (min/ max/ avg)
     * @return symmetrisierte Matrix
     */
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

    /**
     * Findet das Maximum von zwei Werten a und b
     *
     * @param a
     * @param b
     * @return Maximum
     */
    private static double findMin(double a, double b) {
        if (a < b) {
            return a;
        } else {
            return b;
        }
    }

    /**
     * Findet das Minimum von zwei Werten a und b
     *
     * @param a
     * @param b
     * @return Minimum
     */
    private static double findMax(double a, double b) {
        if (a > b) {
            return a;
        } else {
            return b;
        }
    }
}

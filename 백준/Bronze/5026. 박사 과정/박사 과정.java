import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        for (int n = 0 ; n < N ; n++){
            String line = br.readLine();
            if (line.equals("P=NP")){
                bw.write("skipped\n");
            } else {
                String[] parts = line.split("\\+");
                int a = Integer.parseInt(parts[0]);
                int b = Integer.parseInt(parts[1]);
                bw.write(a+b+"\n");
            }
        }

        bw.flush();
        bw.close();
    }
}

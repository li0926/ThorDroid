package sdu.edu.tools;

public class JudgeSystem {
    public static boolean isLinux(){
        return System.getProperty("os.name").toLowerCase().contains("linux");
    }
}

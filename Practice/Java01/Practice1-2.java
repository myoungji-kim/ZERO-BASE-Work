import java.util.Scanner;

public class Practice2 {
    // 내 답안
    public static void solution(char c) {
        int result = c;
        // 대문자
        if (65 <= c && c <= 96) {
            result = c + 32;
        }
        // 소문자
        else if (97 <= c && c <= 128) {
            result = c - 32;
        }
        System.out.println((char) result);
    }

    // 다른 풀이 => 굳이 숫자를 안 외워도 char을 정수값으로 바꾸면 되네..?!
    public static void solution2() {
        Scanner sc = new Scanner(System.in);
        System.out.print("알파벳 입력: ");
        char input = sc.nextLine().charAt(0);
        int output = 0;
        int step = (int) 'a' - (int) 'A';
        if (input >= 'a' & input <= 'z') {
            output = (int) input - step;
            System.out.println("대문자 변환: " + (char) output);
        } else if (input >= 'A' && input <= 'Z') {
            output = (int) input + step;
            System.out.println("소문자 변환: " + (char) output);
        } else {
            System.out.println("입력하신 값이 알파벳이 아닙니다.");
        }
    }

    public static void reference() {
        int a = (int)'a';
        System.out.println("a = " + a);
        int z = (int)'z';
        System.out.println("z = " + z);
        int A = (int)'A';
        System.out.println("A = " + A);
        int Z = (int)'Z';
        System.out.println("Z = " + Z);
        int etc = (int)'%';
        System.out.println("etc = " + etc);
    }

    public static void main(String[] args) {
        reference();    // 아스키 코드 참고
        solution('a');
        solution('b');
        solution('C');
        solution('D');
    }
}

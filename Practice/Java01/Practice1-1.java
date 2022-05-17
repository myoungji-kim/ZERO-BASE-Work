// 입력된 정수 자료형의 숫자를 거꾸로 변환하는 프로그램
public class Practice1 {
    // 내 답안 => 문자열로 변환해서 파악하기
    public static void solution(int num) {
        boolean isMinus = num < 0 ? true : false;

        // string 변환
        String temp = isMinus ? Integer.toString(num).substring(1) : Integer.toString(num);
        StringBuffer sb = new StringBuffer(temp);

        // reverse
        sb = isMinus ? sb.reverse().insert(0, '-') : sb.reverse();

        // print
        System.out.println(Integer.parseInt(sb.toString()));
    }

    // 다른 풀이 => 숫자 자체에서 10을 나누고 곱하면서 뒤집기
    public static void solution2(int num) {
        int numReverse = 0;
        boolean isMinus = false;
        if (num < 0) {
            isMinus = true;
            num *= -1;
        }

        while (num > 0) {
            int r = num % 10;
            num /= 10;
            numReverse = numReverse * 10 + r;
        }
        System.out.println(isMinus ? numReverse * -1 : numReverse);
    }


    public static void main(String[] args) {
        // Test code
        solution(12345);
        solution(-12345);
        solution(100);
        solution(0);
    }
}

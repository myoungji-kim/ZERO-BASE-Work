
public class Practice4 {
    // 내 답안
    public static void solution(int n, int type) {
        if (type == 1) {
            type1(n);
        } else if (type == 2) {
            type2(n);
        } else if (type == 3) {
            type3(n);
        } else if (type == 4) {
            type4(n);
        } else if (type == 5) {
            type5(n);
        }
    }

    // 정사각형
    public static void type1(int n) {
        System.out.println("== Type1 ==");
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < n; i++) {
            sb.append("*");
        }
        for (int i = 0; i < n; i++) {
            System.out.println(sb);
        }
        System.out.println();
    }

    public static void type11(int n) {
        System.out.println("== Type1-2 ==");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.println("*");
            }
            System.out.println();
        }
        System.out.println();
    }

    // 좌측 정렬
    public static void type2(int n) {
        System.out.println("== Type2 ==");
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < n; i++) {
            sb.append("*");
            System.out.println(sb);
        }
        System.out.println();
    }

    // 좌측 정렬
    public static void type22(int n) {
        System.out.println("== Type2-2 ==");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        System.out.println();
    }

    // 우측 정렬
    public static void type3(int n) {
        System.out.println("== Type3 ==");
        StringBuffer sb = new StringBuffer();
        StringBuffer star = new StringBuffer();
        for (int i = 0; i < n; i++) {
            sb = sb.append(" ");
        }
        for (int i = n - 1; i >= 0; i--) {
            sb = sb.replace(i, n + 1, "*");
            for (int j = 1; j < n - i; j++) {
                sb.append("*");
            }
            System.out.println(sb);
        }
        System.out.println();
    }

    public static void type33(int n) {
        System.out.println("== Type3-2 ==");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j < n - i - 1) {
                    System.out.print(" ");
                } else {
                    System.out.print("*");
                }
            }
            System.out.println();
        }
        System.out.println();
    }

    // 산
    public static void type4(int n) {
        System.out.println("== Type4 ==");
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < n; i++) {
            sb.append(" ");
        }
        for (int i = n - 1; i >= 0; i--) {
            sb = sb.replace(i, n + 1, "*");
            for (int j = 1; j < n - i; j++) {
                sb.append("*");
                sb.append("*");
            }
            System.out.println(sb);
        }
        System.out.println();
    }

    public static void type44(int n) {
        System.out.println("== Type4-2 ==");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < i * 2 + 1; j++) {
                System.out.println("*");
            }
            System.out.println();
        }
        System.out.println();
    }

    // 다이아몬드
    public static void type5(int n) {
        System.out.println("== Type5 ==");
        for (int i = 1; i <= n / 2 + 1; i++) {
            StringBuffer sb = new StringBuffer();
            for (int j = 0; j < Math.abs((n / 2) - i + 1); j++) {
                sb.append(" ");
            }
            for (int j = 0; j < (i * 2) - 1; j++) {
                sb.append("*");
            }
            System.out.println(sb);
        }
        for (int i = n / 2; i >= 1; i--) {
            StringBuffer sb = new StringBuffer();
            for (int j = 0; j < Math.abs((n / 2) - i + 1); j++) {
                sb.append(" ");
            }
            for (int j = 0; j < (i * 2) - 1; j++) {
                sb.append("*");
            }
            System.out.println(sb);
        }

        System.out.println();
    }

    public static void type55(int n) {
        System.out.println("== Type5-2 ==");
        // 상단부
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < n / 2 - i; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < i * 2 + 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        // 하단부
        for (int i = n/2; i > 0; i--) {
            for (int j = 0; j < n / 2 + 1 - i; j++) {
                System.out.print(" ");
            }
            for (int j = 0; j < i * 2 - 1; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // Test code
        solution(3, 1);
        solution(3, 2);
        solution(3, 3);
        solution(3, 4);
        solution(7, 5);
    }
}

// 문자 입력 및 출력

public class Practice4 {
    public static String solution(int[] keyLog) {
        final int BACK_SPACE = 8;
        final int SHIFT = 16;
        final int CAPS_LOCK = 20;
        final int SPACE_BAR = 32;
        final int KEY_LEFT = 37;
        final int KEY_RIGHT = 39;
        final int INSERT = 155;
        final int DELETE = 127;
        StringBuffer left = new StringBuffer();
        StringBuffer right = new StringBuffer();
        boolean onShift = false;
        boolean onCapsLock = false;
        boolean onInsert = false;

        for (int key : keyLog) {
            if (key == BACK_SPACE) {
                System.out.println("Case 0");
                left.deleteCharAt(left.length() - 1);

            } else if (key == SHIFT) {
                System.out.println("Case 1");
                onShift = onShift ? false : true;

            } else if (key == CAPS_LOCK) {
                System.out.println("Case 2");
                onCapsLock = onCapsLock ? false : true;

            } else if (key == SPACE_BAR) {
                System.out.println("Case 3");
                left.append(" ");

            } else if (key == KEY_LEFT && left.length() != 0) {
                System.out.println("Case 4");
                right.insert(0, left.charAt(left.length() - 1));
                left.deleteCharAt(left.length() - 1);

            } else if (key == KEY_RIGHT && right.length() != 0) {
                System.out.println("Case 5");
                left.append(right.charAt(right.length() - 1));
                right.deleteCharAt(right.length() - 1);

            } else if (key == INSERT) {
                System.out.println("Case 6");
                onInsert = onInsert ? false : true;

            } else if (key == DELETE) {
                System.out.println("Case 7");
                right = right.deleteCharAt(0);

            } else if (97 <= key && key <= 122) {
                System.out.println("Case 8");
                // 소문자
                if ((onCapsLock && onShift) || (!onCapsLock && !onShift)) {
                    left.append((char) (key));
                }
                // 대문자
                else if ((onCapsLock && !onShift) || (!onCapsLock && onShift)) {
                    left.append((char) (key - 32));
                }
                onShift = false;
                if (onInsert) {
                    right.deleteCharAt(0);
                }

            } else if (48 <= key && key <= 57) {
                System.out.println("Case 9");
                left.append((char) key - 48);
                if (onInsert) {
                    right.deleteCharAt(0);
                }
                onShift = false;
            }

//            System.out.println(left.toString() + right.toString());
//            System.out.println("key: " + key);
        }

        return left.toString() + right.toString();
    }

    public static String solution2(int[] keyLog) {
        final int BACK_SPACE = 8;
        final int SHIFT = 16;
        final int CAPS_LOCK = 20;
        final int SPACE_BAR = 32;
        final int KEY_LEFT = 37;
        final int KEY_RIGHT = 39;
        final int INSERT = 155;
        final int DELETE = 127;

        StringBuffer sb = new StringBuffer();

        int step = (int) ('a' - 'A');

        int cursor = 0;
        int cmdIdx = 0;
        boolean isShift = false;
        boolean isCapsLock = false;
        boolean isInsert = false;
        while (cmdIdx != keyLog.length) {
            int cur = keyLog[cmdIdx];
            if (cur == BACK_SPACE) {
                if (cursor == 0) {
                    cmdIdx++;
                    continue;
                }
                sb.delete(cursor - 1, cursor);
                cursor = Math.max(0, cursor - 1);
            } else if (cur == SHIFT) {
                isShift = true;
            } else if (cur == CAPS_LOCK) {
                isCapsLock = !isCapsLock;
            } else if (cur == SPACE_BAR) {
                inputData(sb, ' ', cursor, isInsert);
                cursor += 1;
            } else if (cur == KEY_LEFT) {
                cursor = Math.max(0, cursor - 1);
            } else if (cur == KEY_RIGHT) {
                cursor = Math.min(sb.length(), cursor + 1);
            } else if (cur == INSERT) {
                isInsert = !isInsert;
            } else if (cur == DELETE) {
                if (cursor == sb.length()) {
                    cmdIdx++;
                    continue;
                }
                sb.delete(cursor, cursor + 1);
            } else if (cur >= 97 && cur <= 122) {
                int data = cur;

                if (isCapsLock && isShift) {
                    data = cur;
                } else if (isCapsLock || isShift) {
                    data -= step;
                }
                inputData(sb, (char) data, cursor, isInsert);
                isShift = false;
                cursor += 1;

            } else if (cur >= 48 && cur <= 57) {
                if (isShift) {
                    char[] specialKey = {')', '!', '@', '#', '$', '%', '^', '&', '*', '('};
                    inputData(sb, specialKey[cur - '0'], cursor, isInsert);
                } else {
                    inputData(sb, (char) cur, cursor, isInsert);
                }
                 // 데이터 입력

                isShift = false;
                cursor += 1;
            }
            cmdIdx++;

        }

        return sb.toString();
    }

    public static void inputData(StringBuffer sb, char data, int cursor, boolean isInsert) {
        if (isInsert == false) {
            sb.insert(cursor, data);
        } else {
            sb.setCharAt(cursor, data);
        }
    }

    public static void main(String[] args) {
        // Test code
        int[] keyLog = {16, 106, 101, 108, 108, 111, 37, 37, 37, 37, 37, 155, 16, 104};
        System.out.println(solution2(keyLog));

        keyLog = new int[]{20, 104, 16, 105, 32, 20, 16, 106, 97, 118, 97};
        System.out.println(solution2(keyLog));

        keyLog = new int[]{49, 51, 8, 50, 51, 53, 55, 37, 37, 127, 127, 52, 53};
        System.out.println(solution2(keyLog));

        keyLog = new int[]{20, 97, 98, 16, 99, 16, 100, 16, 49, 16, 50, 16, 51};
        System.out.println(solution2(keyLog));
    }
}

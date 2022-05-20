// 키보드 자판 

import java.util.ArrayList;

public class Practice3 {
    // 내 답안
    public static String solution(String input, String cmd) {
        StringBuffer left = new StringBuffer(input);
        StringBuffer right = new StringBuffer();
        String[] cmdList = cmd.split(" ");
        boolean isP = false;
        for (String c : cmdList) {
            if (c.equals("L") && left.length() != 0) {
                right.insert(0, left.charAt(left.length() - 1));
                left.deleteCharAt(left.length() - 1);
            } else if (c.equals("D") && right.length() != 0) {
                left.append(right.charAt(0));
                right.deleteCharAt(0);
            } else if (c.equals("B") && left.length() != 0) {
                left.deleteCharAt(left.length() - 1);
            } else if (c.equals("P")) {
                isP = true;
            } else {
                if (isP) {
                    left.append(c);
                    isP = false;
                }
            }
        }
        return left.toString() + right.toString();
    }

    // 다른 풀이
    public static String solution2(String input, String cmd) {
        StringBuffer sb = new StringBuffer(input);
        ArrayList<String> cmdArr = new ArrayList<>();

        for (String s : cmd.split(" ")) {
            cmdArr.add(s);
        }
        int cursor = sb.length();
        int cmdIdx = 0;
        while (cmdIdx != cmdArr.size()) {
            String cur = cmdArr.get(cmdIdx);
            if (cur.equals("L")) {
                cursor = Math.max(0, cursor - 1);
            } else if (cur.equals("D")) {
                cursor = Math.min(sb.length(), cursor + 1);
            } else if (cur.equals("B")) {
                if (cursor == 0) {
                    cmdIdx++;
                    continue;
                }
                sb.delete(cursor - 1, cursor);
                cursor = Math.max(0, cursor - 1);
            } else if (cur.equals("P")) {
                String s = cmdArr.get(++cmdIdx);
                sb.insert(cursor, s);
                cursor += 1;
            }
            cmdIdx ++;
        }
        return sb.toString();
    }


    public static void main(String[] args) {
        // test code
        System.out.println(solution("aba", "L B"));
        System.out.println(solution("abcd", "P x L P y"));
        System.out.println(solution("abc", "L L L P x L B P y"));
        System.out.println(solution("a", "B B L L D D P a P b P c"));
    }
}

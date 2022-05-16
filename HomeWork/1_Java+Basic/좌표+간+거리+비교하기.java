import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Work02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] xy = new char[]{'x', 'y'};

        // 나의 좌표 값 입력
        int[] myCoor = new int[2];
        for (int i = 0; i < xy.length; i++) {
            System.out.print("나의 " + xy[i] + "값 입력: ");
            myCoor[i] = sc.nextInt();
            sc.nextLine();
        }

        // 입력 받은 좌표 값 입력
        final int MAXLENGTH = 10;
        int cnt = 1;
        int[] nearCoor = new int[2];
        int nearDistance = 0;
        ArrayList<int[]> optionCoorList = new ArrayList<>();
        while (cnt <= MAXLENGTH) {
            // 임의의 값 입력
            int[] optionCoor = new int[2];
            for (int i = 0; i < xy.length; i++) {
                System.out.print(cnt + "-" + (i + 1) + ". 임의의 " + xy[i] + "값 입력: ");
                optionCoor[i] = sc.nextInt();
                sc.nextLine();
            }

            // 동일한 값 입력했는지 체크 (isContain)
            boolean isContain = false;
            for (int[] optionCoor2 : optionCoorList) {
                if (Arrays.equals(optionCoor, optionCoor2)) {
                    System.out.println("해당 좌표는 이미 입력하셨습니다. 다시 입력해 주세요.");
                    isContain = true;
                    break;
                }
            }

            // 새로운 값을 입력했다면 -> 리스트에 추가 및 나의 좌표 값과 거리 비교
            if (!isContain) {
                int distance = Math.abs(myCoor[0] - optionCoor[0]) + Math.abs(myCoor[1] - optionCoor[1]);
                if (cnt == 1){ // 첫 입력
                    nearCoor[0] = optionCoor[0];
                    nearCoor[1] = optionCoor[1];
                    nearDistance = distance;
                } else {
                    if (distance < nearDistance) { // 최소 거리 값이라면
                        nearDistance = distance;
                        nearCoor[0] = optionCoor[0];
                        nearCoor[1] = optionCoor[1];
                    }
                }
                optionCoorList.add(optionCoor);
                cnt++;
            }
        }

        System.out.println("나의 좌표 값: " + Arrays.toString(myCoor));
        System.out.print("임의의 좌표 값: ");
        for (int[] optionCoor : optionCoorList) {
            System.out.print(Arrays.toString(optionCoor) + " ");
        }
        System.out.println("\n나의 좌표와 가장 가까운 좌표는: " +Arrays.toString(nearCoor));
        System.out.println("가까운 좌표와 내 좌표와의 거리는: "+nearDistance);
    }
}

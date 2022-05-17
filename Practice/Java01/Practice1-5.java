// 물을 가장 많이 담을 수 있는 두 벽 고르기
public class Practice5 {
    // 내 답안
    public static int solution(int[] height) {
        int bigSize = 0;
        int[] wallNum = new int[2];
        for (int w1 = 0; w1 < height.length; w1++) {
            for (int w2 = w1; w2 < height.length; w2++) {
                int size = height[w1] <= height[w2] ? (w2 - w1) * height[w1] : (w2 - w1) * height[w2];
                if (bigSize < size) {
                    bigSize = size;
                    wallNum[0] = w1;
                    wallNum[1] = w2;
                }
            }
        }
//        System.out.println(wallNum[0] + 1);
//        System.out.println(wallNum[1] + 1);
        return bigSize;
    }

    // 다른 풀이
    public static int solution2(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int x = (right - left);
            int y = height[left] < height[right] ? height[left] : height[right];
            int curArea = x * y;
            maxArea = maxArea > curArea ? maxArea : curArea;

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxArea;
    }

    public static void main(String[] args) {
        // Test code
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println(solution(height));

        height = new int[]{5, 3, 9, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2};
        System.out.println(solution(height));

    }
}

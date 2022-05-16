public class Work03 {
    public static void main(String[] args) {
        long totalNumPost = 127; // 전체 게시글 수
        long nowPage = 11; // 현재 페이지

        Pager pager = new Pager(totalNumPost);
        System.out.println(pager.html(nowPage));
    }
}

public class Pager {
    final long PERPOSTNUM = 10; // 한 페이지 당 게시글 수
    final long PERBLOCKNUM = 10; // 한 블럭 당 페이지 수
    long totalNumPost; // 전체 게시글 수
    long nowPage; // 현재 페이지
    long totalPageNum; // 전체 페이지 수
    long startPage; // 블럭에서 시작하는 페이지 번호
    long endPage; // 블럭에서 끝나는 페이지 번호
    long startPost; // 페이지에서 시작하는 게시글 번호
    long endPost; // 페이지에서 끝나는 게시글 번호

    // Constructor
    public Pager(long totalNumPost) {
        this.totalNumPost = totalNumPost;
        this.nowPage = nowPage;
        this.totalPageNum = getTotalPageNum(totalNumPost);
    }

    // 전체 페이지 수
    public long getTotalPageNum(long totalNumPost) {
        return totalNumPost % PERPOSTNUM == 0 ? totalNumPost / PERPOSTNUM : totalNumPost / PERPOSTNUM + 1;
    }

    // 블럭에서 시작하는 페이지 번호
    public long getStartPage(long nowPage) {
        return nowPage % PERBLOCKNUM == 0 ? nowPage / PERBLOCKNUM: (nowPage / PERBLOCKNUM) * PERBLOCKNUM + 1;
    }

    // 블럭에서 끝나는 페이지 번호
    public long getEndPage(long nowPage) {
        long EndBlockNum = nowPage % PERBLOCKNUM == 0 ? nowPage : (nowPage / 10 + 1) * PERBLOCKNUM;
        return EndBlockNum > totalPageNum ? totalPageNum : EndBlockNum;
    }

    // 페이지에서 시작하는 게시글 번호
    public long getStartPost(long nowPage) {
        return ((nowPage - 1) * PERPOSTNUM) + 1;
    }

    // 페이지에서 끝나는 게시글 번호
    public long getEndPost(long nowPage) {
        long EndPostNum = nowPage * PERPOSTNUM;
        return EndPostNum > totalNumPost ? totalNumPost : EndPostNum;
    }

    // 결과
    public String html(long nowPage) {
        this.startPage = getStartPage(nowPage);
        this.endPage = getEndPage(nowPage);
        this.startPost = getStartPost(nowPage);
        this.endPost = getEndPost(nowPage);

        String code = "";
        // 처음, 이전
        code += "<a href='#'>[처음]</a>\n" +
                "<a href='#'>[이전]</a>\n\n";
        
        // 페이징
        for (long i = this.startPage; i <= this.endPage; i++) {
            code += i == nowPage ? "<a href='#' class='on'>" : "<a href='#'>";
            code += i;
            code += "</a>\n";
        }
        
        // 다음, 마지막
        code += "\n<a href='#'>[다음]</a>\n" +
                "<a href='#'>[마지막]</a>";
        return code;
    }
}

public class Solution {
    public int NumJewelsInStones(string J, string S) {
        int num = 0;
        bool[] letters = new bool[128];
        char[] Jc = J.ToCharArray();
        foreach(char l in Jc) {
            letters[l] = true;
        }
        char[] Sc = S.ToCharArray();
        foreach(char l in Sc) {
            if (letters[l]) 
                num ++;
        }
        return num;
    }
}
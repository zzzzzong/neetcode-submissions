func groupAnagrams(strs []string) [][]string {
    // sorted x hashmap, time: O(), space: O() 

    ans := make([][]string, 0, len(strs))
    hmap := make(map[string][]string, len(strs))
    
    // prepare the hashmap
    for _, word := range strs {
        var counter [26]byte    // byte == uint8, 最輕量 看註解

        for i := 0; i < len(word); i++ {
            counter[word[i]-'a']++
        }
        
        key := string(counter[:])
        hmap[key] = append(hmap[key], word)
    }

    // join the ans and return
    for _, val := range hmap {
        ans = append(ans, val)
    }

    return ans
}


/*
在 Go 語言中，數值型別（數字）主要分為以下三大類：
1. 整數型別 (Integers)
有號整數 (可正可負)： int8, int16, int32, int64
無號整數 (只能正數/零)： uint8 (別名 byte), uint16, uint32, uint64
平台相關 (32或64位元)： int, uint, uintptr (指標)
萬國碼字元： rune (別名 int32)

2. 浮點數型別 (Floats / 小數)
float32 (單精度)float64 (雙精度，最常用)

3. 複數型別 (Complex)
complex64, complex128 (用於工程與數學計算)
*/

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int f = 0;
        int e = arr.size()-1;
        int mid = f + (e-f)/2;
        int c;
        while(f<e)
        {
            if(arr[mid] < arr[mid+1])
            {
                f = mid+1;
            }
            else{
                e=mid;
            }
            mid = f+ (e-f)/2;
        }
        return f;
    }
};
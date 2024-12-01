
int getsong(vector<int>&arr,int &c){
    int n = arr.size();
    int randindx = math.rand(*(n-c));
    swap(arr[randindx],arr[n-1-c]);
    c++;
}

void playmusic(vector<int>&arr){
    int last = arr.size()-1;
    int n = arr.size();
    int count = 0;
    // for(int i=0;i<n;i++){
    //     int randindx = math.rand(*(n-count));

    //     playsond();

    //     swap(arr[randindx],arr[last-count]);

    //     count++;
    // }
    int getindex = getsong(arr,count);

    return getindex;
}

int main(){
    int n;
    cin>>n;

    vector<int>arr;
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    playmusic(arr);
}

// 1 2 3 10 11 12 --> 0 1 3 0 1 2 
// 0 1 2  3  4  5
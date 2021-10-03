#include<iostream>
#include<vector>

using namespace std;

int main(){
    int size;
    vector<int> vec;
    int val;
    int evenCount = 0;
    int oddCount = 0;
    cin>>size;

    for(int i=0;i<size;i++){
        cin>>val;
        vec.push_back(val);
    }

    for(int i=0;i<vec.size();i++){
        if(vec[i]%2 == 0)
            evenCount++;
        else
            oddCount++;
    }
    if(evenCount > oddCount)
        cout<<"READY FOR BATTLE"<<endl;
    else
        cout<<"NOT READY"<<endl;

    return 0;
}
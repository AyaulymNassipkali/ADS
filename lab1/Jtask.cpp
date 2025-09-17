#include <iostream>
#include <deque>
using namespace std;

int main(){
    /*
    +1
    -9
    +2
    *
    +2
    -6
    +3
    -9
    *
    *
    *
    * 
    !
    2 1 9 -> 11
    3 2 1 6 9 
    12
    8
    */
   char c; int  a;
   deque<int> dq;

   while(true){
    cin>>c;
    if(c=='+'){
        cin>>a;
        dq.push_front(a);
    }
    else if(c=='-'){
    cin >> a;
    dq.push_back(a); 
    }
    else if(c == '*'){
        if(dq.size() == 0) cout << "error\n";
        else{
            cout<<dq.front() + dq.back() << '\n';
            if(dq.size()>=2){
                dq.pop_front();dq.pop_back();
            } else dq.pop_front();
        }
    }
    else break;
   }
   return 0;
}
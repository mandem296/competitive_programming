class Solution{
         public:
    int select(int arr[], int i)
    {
        return arr[i];
    }
     
    void selectionSort(int arr[], int n)
    {
       int element=0;
       for(int j=0; j<4;j++){
           if(arr[j]>arr[j+1]){
               element=arr[j];
               arr[j]=arr[j+1];
               arr[j+1]=element;
           }
       }
    }
};

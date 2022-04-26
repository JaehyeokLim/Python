// n = 0 or not 0 or not 0 or not 1 or not 1
// n1 = 0 or not 1 or not 0 or not 1 or not 1 
// print(n1)
// print(n)
// // 에러 검출 코드
// #include <iostream>
// using namespace std;

// int main()
// {
// 	char input[7];
// 	cin >> input;
// 	cout << “input :” << input << endl;

// 	char crc[4] = “000”;
// 	char bit = 0;

// 	for (int i = 0; i<6; i++){
// 		if (input[i] == crc[0]){
// 			bit = ‘0’;
// 		}
// 		else{
// 			bit = ‘1’;
// 		}			
// 		if(bit == crc[1]){
// 			crc[0] = ‘0’;
// 		}
// 		else{
// 			crc[0] = ‘1’;
// 		}
// 		crc[1] = crc[2];
// 		crc[2] = bit;
// 		cout << i << “ : “ << crc << endl;
// 	}
// 	cout << “FCS: “ << crc << endl;
// }
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//单个字符转成十进制
int hex(char c)
{
    if(c>='0'&&c<='9')
        return c-'0';
    else if(c>='a'&&c<='f')
        return (10+(c-'a'));
    else
        return -1;
}
//对每个字符解密
int cp(char bf1,char bf2)
{
        int t1,t2;
        t1=hex(bf1);
        t2=hex(bf2);
        if(t1==-1||t2==-1)
        {
            printf("what the hell!");
            return -1;
        }
        else
            return 127^(t1*16+t2);//关键代码
}
int main()
{
    puts("拨开乌云出品!");
    char buff[100],t1,t2;
    int len,ans,i;
    //读写数据
    freopen("mima.in", "r", stdin);
	freopen("siwa.out", "w", stdout);
    while(scanf("%s",buff)!=EOF)
    {
        len = strlen(buff);
        for(i=0;i<len;i++)
        {
            t1=buff[i];
            ++i;
            t2=buff[i];
            ans=cp(t1,t2);
            if(ans==-1)
            {
                printf("some thing wrong!...");
                return 0;
            }
            printf("%c",ans);//输出每个解密后的字符
        }
        puts("");
    }
    fclose(stdin);
	fclose(stdout);
	return 0;
}

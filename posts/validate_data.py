from .models import Post
#기존의 데이터를 새로 추가된 유효성 검사 로직에 맞춰주는 

def validate_post():
    #1 모든 포스트 데이터 가져오기
    posts = Post.objects.all()
    #2 각각의 포스트 데이터를 보면서 내용 안에 &가 있는지 체크하기
    for post in posts:
        if '&' in post.content:
            print(post.id, '번 글에 &가 있습니다.')
    #3 만약 &가 있다면 해당 &를 삭제 처리
            post.content.replace('&','')
            post.save()
        if post.dt_modified<post.dt_created:
            print(post.id, '번 글의 수정일이 생성일보다 과거입니다')
            post.save()

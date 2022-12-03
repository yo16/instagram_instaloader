import instaloader
import os

def main():
    loader = instaloader.Instaloader()
    loader.login(os.environ['INSTAGRAM_ID'], os.environ['INSTAGRAM_PASSWORD'])
    
    print('aa')


if __name__=='__main__':
    from set_env import set_env
    set_env()
    main()

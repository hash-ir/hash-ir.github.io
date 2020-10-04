import os
import sys
import frontmatter

def generate_tag_slug():
    '''
    Iterates through the posts' frontmatter, collects tags and creates 
    tag slugs in _data/tags.yml in the following format:
    - slug: <tag_name>
    '''

    root_dir = get_root_dir()
    posts_dir = os.path.join(root_dir, '_posts')
    drafts_dir = os.path.join(root_dir, '_drafts')
    
    # read lines from _data/tags.yml
    with open(os.path.join(root_dir, '_data/tags.yml'), 'r') as f:
        existing_tags = f.readlines()

    # get actual tags without the '- slug:' prefix
    existing_tags = [tag.split(':')[1].strip() for tag in existing_tags]

    # open _data/tags.yml in append mode
    f = open(os.path.join(root_dir, '_data/tags.yml'), 'a')

    flag = 0
    print('Generating tag slugs...')
    for dir in [posts_dir, drafts_dir]:
        print('Fetching posts from {}'.format(dir))

        for post in os.listdir(dir):
            
            # get tags in the frontmatter of post 
            tags = get_post_tags(post, dir)

            for tag in tags:

                # create a tag slug if it does not exist
                if tag not in existing_tags:
                    f.write('- slug: '+tag)
                    f.write('\n')
                    print('Added {} to data/tags.yml'.format(tag))
                    flag = 1
        print()

    f.close()

    # already updated
    if not flag:
        print('No tag slugs added!')
    

def generate_tag_markdown():
    '''
    Iterates through the tags in _data/tags.yml and creates 
    empty markdown template in blog/tag/ in the following format:
    ---
    layout: by_tag
    tag: <tag_name>
    permalink: /blog/tag/<tag_name>/
    ---
    '''

    # read lines from _data/tags.yml
    with open('.././_data/tags.yml', 'r') as f:
        tags = f.readlines() 

    # get actual tags without the '- slug:' prefix
    tags = [tag.split(':')[1].strip() for tag in tags]

    flag = 0
    print('Generating tag layouts...')
    for tag in tags:

        # create layout if it does not exist
        if not os.path.isfile(os.path.join('.././blog/tag', tag+'.md')):

            with open(os.path.join('.././blog/tag', tag+'.md'), 'w') as f:
                f.write('---')
                f.write('\n')
                f.write('layout: by_tag')
                f.write('\n')
                f.write('tag: '+tag)
                f.write('\n')
                f.write('permalink: /blog/tag/'+tag+'/')
                f.write('\n')
                f.write('---')

            print('Created empty markdown template for tag: {}'.format(tag))
            flag = 1

    # alread updated
    if not flag:
        print('No layouts generated!')



def get_post_tags(post, posts_dir):
    '''
    Loads frontmatter of the post

    Parameters:
        post (markdown file): name of the file
        posts_dir (path): path of the _posts directory

    Returns:
        post['tags] (List): list of all the tags of a post
    '''
    with open(os.path.join(posts_dir, post), 'r') as f:
        post = frontmatter.load(f)

    return post['tags']

def get_root_dir():
    '''
    Returns the project directory
    '''
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print('Working in {}\n'.format(get_root_dir()))
    generate_tag_slug()
    print()
    generate_tag_markdown()
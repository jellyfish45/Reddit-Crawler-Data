import time 
import praw 
import multiprocessing

reddit = praw.Reddit(
    client_id="54u8-WeUDusPlUoFQDZu4w",
    client_secret="lGhkiE6scCkSMYsj0P9AXzyYVSLBag",
    user_agent="jellyfish"
)

def process_ID(redditor):
    print("redditor is ", redditor)
    try:
        comment_count = redditor.comments.new(limit=1)
        # sub3 = []
        sub_ids = list()
        time.sleep(.3)
        for comment in redditor.comments.new(limit=20):
            # sub3.append(comment.submission)
            sub_ids.append(comment.link_id)
        dic = {}

        #get submission from subids 
        print("getting submissions")
        sub3 = reddit.info(fullnames=sub_ids)
        print("iterating submissions")
        for submission in sub3:
            print("replacing more")
            submission.comments.replace_more(limit=None)
            print("done w/ replacement")
            comments = [comment for comment in submission.comments.list()]
            for comment in comments:
                #I think this is comparing an object to a str (ERROR???)
                if (comment.author != redditor) &(comment.author != None):
                    if comment.author.name not in dic:
                        dic[comment.author.name] = 1
                    else:
                        dic[comment.author.name] += 1

        max_key = max(dic, key=dic.get)
        pair = (redditor, max_key)
        print("dome")
        return pair
    except Exception as e:
        print("Eexception is ", e)
        return None

# filtered_id =  ['MoosieGoose', 'JollyK9', 'Southern_Ad3032', 'bduwowy272habbw', 'Late_Introduction203', 'kapster68', 'TheApertureMonkey', 'talemoon22', 'sebagolindenwald', 'spicyranchplzz', 'TheFloorMayBeLava_02', 'rxtten_flesh', 'greenblooded395', 'greenblooded395', 'DrakenJosh98', 'WhichUsernameIsBest', 'FStahp2', 'Pongpianskul', 'Kanashimi515', 'eviuwu', 'Kattheloner_22', 'Reeze2911', 'Sac20000', 'RanpoWasTaken', 'jlynny1811', 'Playful-Fail4778', 'GarageOk8109', 'katandcats', 'holyredemption', 'jifpeanutbutter420', 'Timely_Inflation1000', 'Erica_Peanut']
filtered_id = ['MoosieGoose', 'JollyK9', 'Southern_Ad3032', 'bduwowy272habbw']
filtered_id = [reddit.redditor(i) for i in filtered_id]

def main():
    with multiprocessing.Pool(4) as pool:
        
        results = list()
        for k in filtered_id:
            results.append(pool.apply_async(process_ID, (k,)))

        final_reusults = list()
        for result in results:
            print("getting result")

            final_reusults.append(result.get())

        print("\n"*10)
        for f in final_reusults:
            print(f)


        # pool.join()

if __name__ == '__main__':
    main()
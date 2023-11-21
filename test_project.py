import project


def test_get_youtube_video_transcripts():
    assert (
        project.get_youtube_video_transcripts(
            "https://www.youtube.com/watch?v=U20LO-20Eco"
        )
        == "for our next story let's talk about another War not a war on ground but a war against inflation Global inflation seems to have turned a corner inflation rates are falling in the United States in the UK and also in the Euro zone for central banks it's a major relief they still remain wary but right now the economy is looking better the question is how did it happen how did the world win this war against inflation India's external affairs minister says the world has India to thank for it why our next report answers that question yesterday the UK came out with its inflation figures they've been bad for quite some time but yesterday was a welcome change why because inflation in the UK has dropped to 4.6% that's the lowest in the last 2 years but it's not not just the UK that's witnessing falling inflation rates there's the United States inflation has cooled off there too in October it's 3.2% in the Euro Zone it was around 3% so three major economies are all witnessing falling inflation rates does that mean that we've won the war against inflation well not so soon the central banks are happy but not too much they still remain wary so how did global infl turn a corner suddenly well the reasons are many let's look at what drove the prices up there was the covid-19 pandemic then the unprecedented stimulus by governments and finally the Russia Ukraine war all of that affected the prices and all of that drove up the prices which brings us to the central banks they may be happy now but they've been hawkish in the past 2 years hiking interest rates to curb inflation it might have been been a divisive approach then but it looks like it worked even with the most stubborn inflation rates but while Global inflation rates cool off India's external affairs minister had something to say he says the world has India to thank for this here's why J Shanker says India bought oil from Russia despite sanctions if it didn't oil prices would be higher New Delhi and Europe would be battling for the same suppliers and all that would do is drive up the prices so the world has India to thank for keeping oil prices steady had we not B bought oil from Russia I think o the global oil prices would have gone higher because we would have gone into the same Market to the same suppliers that Europe would have done and frankly as we discovered Europe would have out priced us and in fact uh at least India was a uh big enough country uh to to command some resp expect in the markets but there were much smaller countries who didn't even get responses to the tender inquiries because the LM suppliers were no longer interested in dealing with them they have bigger fish to fry so we've actually softened the oil markets uh and the gas markets through uh our uh purchase policies we have as a consequence actually managed Global inflation so frankly people should be India is the third largest crude consumer after the United States and China so if India didn't buy from Russia it would drive up prices simple demand and Supply the more the demand the less the supply the higher the prices and it wasn't just India it was the whole of the global South they Protected Their Own interests and that has made a whole lot of difference "
    )


def test_get_youtube_video_title():
    assert (
        project.get_youtube_video_title("https://www.youtube.com/watch?v=U20LO-20Eco")
        == "India to Thank for Falling Inflation? Here's What S. Jaishankar Said | Vantage with Palki Sharma "
    )


def test_connect_to_llama():
    assert (
        project.connect_to_llama(
            project.get_youtube_video_transcripts(
                "https://www.youtube.com/watch?v=U20LO-20Eco"
            ),
            project.get_youtube_video_title(
                "https://www.youtube.com/watch?v=U20LO-20Eco"
            )
        )
        == False
    )

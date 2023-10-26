def convert_minute(time):
    hour, minute = map(int, time.split(":"))
    return (hour * 60) + minute

def convert_code(text):
    return text.replace("C#", "c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#", "a")

def solution(m, musicinfos):
    answer = []
    m = convert_code(m)
    
    for idx, info in enumerate(musicinfos):
        start, end, name, code = info.split(",")
        playing_time = convert_minute(end) - convert_minute(start)

        music = convert_code(code)
        
        if playing_time < len(music):
            music = music[:playing_time]
        else:
            q,r = divmod(playing_time, len(music))
            music = music * q + music[:r]
        
        if m in music:
            answer.append([name, playing_time, idx])
        
        
    answer.sort(key=lambda x: (-x[1],x[2]))
    if answer:
        return answer[0][0]
    else:
        return "(None)"
            
            
            
        

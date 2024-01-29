let getM3U8 = () => {
    let m3u8 = document.documentElement.innerHTML.match(/https?:\/\/[^"]*playlist\.m3u8[^"]*/)[0];
    console.log(m3u8);
    navigator.clipboard.writeText(m3u8);
}

getM3U8();

let getVTT = () => {
    let vtt = document.documentElement.innerHTML.match(/https?:\/\/[^"]*\.vtt[^"]*/)[0];
    console.log(vtt);
    navigator.clipboard.writeText(vtt);
}

getVTT();

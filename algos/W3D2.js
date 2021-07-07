/* 
    Given in an alumni interview in 2021.
    String Encode
    You are given a string that may contain sequences of consecutive characters.
    Create a function to shorten a string by including the character,
    then the number of times it appears. 


    If final result is not shorter (such as "bb" => "b2" ),
    return the original string.
    
    const str1 = "aaaabbcddd";
    const expected1 = "a4b2cd3";
    
    const str2 = "";
    const expected2 = "";
    
    const str3 = "a";
    const expected3 = "a";
    
    const str4 = "bbcc";
    const expected4 = "bbcc";
    
    const str5 = "aaaabbcdddaaa";
    const expected5 = "a4b2cd3a3";

    const str6 = "aabbbaaaaccdddd";
    const expected6 = "a2b3a4c2d4";

    const str7 = "hellowoooorld"
    const expected7 = "hel2owo4rld";


*/

/**
 * Encodes the given string such that duplicate characters appear once followed
 * by a number representing how many times the char occurs only if the
 * character occurs more than one time.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str The string to encode.
 * @returns {string} The given string encoded.
*/
function encodeStr(str) {
    var counter = 0;
    var encode = "";
    for (var i = 0; i < str.length; i++) {
        // push first letter 
        // if/else to check if previous element was diff
        if (i == 0) {
            encode += str[i];
            counter++;
        } else if (i == str.length - 1) { //cheks last elem
            counter++;
            encode += counter;
        }
        else if (str[i] == str[i - 1]) {
            counter++;
        } else if (str[i] != str[i - 1]) {
            // check if value at index == previous elem
            encode += counter;
            encode += str[i];
            counter = 1;
        }
        // check if the 2nd is the same => increment counter
    }
    return encode;
}
console.log(encodeStr("aabbbaaaaccdddd"));

/* 
    String Decode  

    const str1 = "a3b2cd3";
    const expected1 = "aaabbcddd";

    const str2 = "a3b2c12d10";
    const expected2 = "aaabbccccccccccccdddddddddd";

    HINT: isNaN(someValue)
    Example: isNaN("yes") => true
    isNaN("8") => false
*/
/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */

function decodeStr(str) {
    // going in reverse! type up the elem by the numer of times
    var letters = ""
    for (var i = 0; i < str.length; i++) {
        if (isNaN(str[i]) == true) {
            // push letter into counter
            letters += str[i];
        } else if (isNaN(str[i]) == false) { //when the elem is a num,
            for (var j = 1; j < str[i]; j++) {// 
                letters += str[i - 1];
            }
        }
    }
    return letters;
}
console.log(decodeStr("a3b2c12d10"));
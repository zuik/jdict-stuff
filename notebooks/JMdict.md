# JMdict

## Data format

- JMdict (entry*)
    - entry (ent_seq, k_ele*, r_ele+, sense+) : an entry in JMdict
        - ent_seq: A unique numeric sequence number for each entry
        - k_ele (keb, ke_inf*, ke_pri*) : The kanji element, or in its absence, the reading element, is 
	the defining component of each entry.
            - keb: This element will contain a word or short phrase in Japanese which is written using at least one non-kana character (usually kanji, but can be other characters). The valid characters are kanji, kana, related characters such as chouon and kurikaeshi, and in exceptional cases, letters from other alphabets. 
            - ke_inf*: This is a coded information field related specifically to the orthography of the keb, and will typically indicate some unusual aspect, such as okurigana irregularity.
            - ke_pri*: This and the equivalent re_pri field are provided to record information about the relative priority of the entry,  and consist of codes indicating the word appears in various references which can be taken as an indication of the frequency with which the word is used. This field is intended for use either by applications which  want to concentrate on entries of  a particular priority, or to  generate subset files. 
        - r_ele (reb, re_nokanji?, re_restr*, re_inf*, re_pri*): The reading element typically contains the valid readings of the word(s) in the kanji element using modern kanadzukai. Where there are multiple reading elements, they will typically be alternative readings of the kanji element. In the absence of a  kanji element, i.e. in the case of a word or phrase written entirely in kana, these elements will define the entry.
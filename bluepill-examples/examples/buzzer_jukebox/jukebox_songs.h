#ifndef __JUKEBOX_SONGS_H
#define __JUKEBOX_SONGS_H

#include "libmusic.h"
#include <stdio.h>

struct Song {
	int length;
	int bpm; /* beats per minute */
	uint8_t *notes_pitch;
	uint8_t *notes_duration;
};

#define JUKEBOX_SONGS_TOTAL_SONGS 45
struct Song jukebox_song_list[JUKEBOX_SONGS_TOTAL_SONGS];

#define SONG_MACGYVER_ORDER 0
#define SONG_LEN_MACGYVER 29
#define SONG_VEL_MACGYVER 160

#define SONG_UNDER_THE_SEA_ORDER 1
#define SONG_LEN_UNDER_THE_SEA 45
#define SONG_VEL_UNDER_THE_SEA 200

#define SONG_BATMAN_ORDER 2
#define SONG_LEN_BATMAN 19
#define SONG_VEL_BATMAN 180

#define SONG_LIGHTMYFIRE_ORDER 3
#define SONG_LEN_LIGHTMYFIRE 33
#define SONG_VEL_LIGHTMYFIRE 140

#define SONG_TEARS_IN_HEAVEN_ORDER 4
#define SONG_LEN_TEARS_IN_HEAVEN 17
#define SONG_VEL_TEARS_IN_HEAVEN 112

#define SONG_AADAMS_ORDER 5
#define SONG_LEN_AADAMS 51
#define SONG_VEL_AADAMS 160

#define SONG_DRNO_ORDER 6
#define SONG_LEN_DRNO 78
#define SONG_VEL_DRNO 112

#define SONG_BA_BA_ORDER 7
#define SONG_LEN_BA_BA 17
#define SONG_VEL_BA_BA 100

#define SONG_GEORGIA_ON_MY_MIND_ORDER 8
#define SONG_LEN_GEORGIA_ON_MY_MIND 22
#define SONG_VEL_GEORGIA_ON_MY_MIND 63

#define SONG_MISSIONIMPOSSI_ORDER 9
#define SONG_LEN_MISSIONIMPOSSI 24
#define SONG_VEL_MISSIONIMPOSSI 180

#define SONG_BEETHOVEN_ORDER 10
#define SONG_LEN_BEETHOVEN 22
#define SONG_VEL_BEETHOVEN 160

#define SONG_FLNTSTN_ORDER 11
#define SONG_LEN_FLNTSTN 35
#define SONG_VEL_FLNTSTN 200

#define SONG_LITHIUM_ORDER 12
#define SONG_LEN_LITHIUM 28
#define SONG_VEL_LITHIUM 40

#define SONG_DEATH_MARCH_ORDER 13
#define SONG_LEN_DEATH_MARCH 11
#define SONG_VEL_DEATH_MARCH 125

#define SONG_DIRE_ORDER 14
#define SONG_LEN_DIRE 27
#define SONG_VEL_DIRE 160

#define SONG_DASBOOT_ORDER 15
#define SONG_LEN_DASBOOT 28
#define SONG_VEL_DASBOOT 100

#define SONG_SUPERMAN_ORDER 16
#define SONG_LEN_SUPERMAN 50
#define SONG_VEL_SUPERMAN 200

#define SONG_GREENDAY_ORDER 17
#define SONG_LEN_GREENDAY 44
#define SONG_VEL_GREENDAY 50

#define SONG_DON_T_WANNA_MISS_A_THING_ORDER 18
#define SONG_LEN_DON_T_WANNA_MISS_A_THING 46
#define SONG_VEL_DON_T_WANNA_MISS_A_THING 125

#define SONG_GIRLFROMIPANE_ORDER 19
#define SONG_LEN_GIRLFROMIPANE 30
#define SONG_VEL_GIRLFROMIPANE 160

#define SONG_KNIGHTRIDER_ORDER 20
#define SONG_LEN_KNIGHTRIDER 64
#define SONG_VEL_KNIGHTRIDER 125

#define SONG_90210_ORDER 21
#define SONG_LEN_90210 37
#define SONG_VEL_90210 140

#define SONG_HALLOWEEN_ORDER 22
#define SONG_LEN_HALLOWEEN 40
#define SONG_VEL_HALLOWEEN 180

#define SONG_CASTLE_ON_A_CLOUD_ORDER 23
#define SONG_LEN_CASTLE_ON_A_CLOUD 35
#define SONG_VEL_CASTLE_ON_A_CLOUD 90

#define SONG_IMPERIAL_ORDER 24
#define SONG_LEN_IMPERIAL 112
#define SONG_VEL_IMPERIAL 112

#define SONG_RICH_ORDER 25
#define SONG_LEN_RICH 30
#define SONG_VEL_RICH 112

#define SONG_AXELF_ORDER 26
#define SONG_LEN_AXELF 23
#define SONG_VEL_AXELF 160

#define SONG_THINK_PINK_ORDER 27
#define SONG_LEN_THINK_PINK 39
#define SONG_VEL_THINK_PINK 70

#define SONG_FIGARO_ORDER 28
#define SONG_LEN_FIGARO 99
#define SONG_VEL_FIGARO 250

#define SONG_ARGENTINA_ORDER 29
#define SONG_LEN_ARGENTINA 39
#define SONG_VEL_ARGENTINA 70

#define SONG_MORE_THAN_WORDS_ORDER 30
#define SONG_LEN_MORE_THAN_WORDS 22
#define SONG_VEL_MORE_THAN_WORDS 90

#define SONG_MICROMELODY_ORDER 31
#define SONG_LEN_MICROMELODY 37
#define SONG_VEL_MICROMELODY 250

#define SONG_SW_END_ORDER 32
#define SONG_LEN_SW_END 41
#define SONG_VEL_SW_END 225

#define SONG_STAIRWAY_ORDER 33
#define SONG_LEN_STAIRWAY 27
#define SONG_VEL_STAIRWAY 63

#define SONG_BEATLES_LET_IT_BE_ORDER 34
#define SONG_LEN_BEATLES_LET_IT_BE 27
#define SONG_VEL_BEATLES_LET_IT_BE 100

#define SONG_GODFATHER_ORDER 35
#define SONG_LEN_GODFATHER 37
#define SONG_VEL_GODFATHER 80

#define SONG_CANTINA_ORDER 36
#define SONG_LEN_CANTINA 52
#define SONG_VEL_CANTINA 250

#define SONG_SWEND_ORDER 37
#define SONG_LEN_SWEND 41
#define SONG_VEL_SWEND 225

#define SONG_EUROPE_ORDER 38
#define SONG_LEN_EUROPE 97
#define SONG_VEL_EUROPE 140

#define SONG_BARBIEGIRL_ORDER 39
#define SONG_LEN_BARBIEGIRL 23
#define SONG_VEL_BARBIEGIRL 125

#define SONG_FUNKYTOWN_ORDER 40
#define SONG_LEN_FUNKYTOWN 25
#define SONG_VEL_FUNKYTOWN 125

#define SONG_LET_IT_BE_ORDER 41
#define SONG_LEN_LET_IT_BE 27
#define SONG_VEL_LET_IT_BE 100

#define SONG_INDIANAJONES_ORDER 42
#define SONG_LEN_INDIANAJONES 55
#define SONG_VEL_INDIANAJONES 250

#define SONG_BOLERO_ORDER 43
#define SONG_LEN_BOLERO 48
#define SONG_VEL_BOLERO 80

#define SONG_XFILES_ORDER 44
#define SONG_LEN_XFILES 44
#define SONG_VEL_XFILES 125

uint8_t init_jukebox_songs(void);
uint8_t get_total_songs_number(void);

#endif /* __JUKEBOX_SONGS_H */

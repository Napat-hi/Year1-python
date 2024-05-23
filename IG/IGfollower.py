Skip to content
 
Search…
All gists
Back to GitHub
Sign in
Sign up
Instantly share code, notes, and snippets.

@abir-taheer
abir-taheer/instagram-follower-following.js
Last active 6 hours ago
Code
Revisions
19
Stars
433
Forks
73
Clone this repository at &lt;script src=&quot;https://gist.github.com/abir-taheer/0d3f1313def5eec6b78399c0fb69e4b1.js&quot;&gt;&lt;/script&gt;
<script src="https://gist.github.com/abir-taheer/0d3f1313def5eec6b78399c0fb69e4b1.js"></script>
"This is our community, this is our family, these are our friends." https://www.youtube.com/watch?v=gk7iWgCk14U&t=425s
instagram-follower-following.js
if (window.location.origin !== "https://www.instagram.com") {
  window.alert(
    "Hey! You need to be on the instagram site before you run the code. I'm taking you there now but you're going to have to run the code into the console again.",
  );
  window.location.href = "https://www.instagram.com";
  console.clear();
}

const fetchOptions = {
  credentials: "include",
  headers: {
    "X-IG-App-ID": "936619743392459",
  },
  method: "GET",
};

let username;

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const random = (min, max) => Math.floor(Math.random() * (max - min)) + min;

// This function handles all of the pagination logic
// Calls the API recursively until there are no more pages to load
const concatFriendshipsApiResponse = async (
  list,
  user_id,
  count,
  next_max_id = "",
) => {
  let url = `https://www.instagram.com/api/v1/friendships/${user_id}/${list}/?count=${count}`;
  if (next_max_id) {
    url += `&max_id=${next_max_id}`;
  }

  const data = await fetch(url, fetchOptions).then((r) => r.json());

  if (data.next_max_id) {
    const timeToSleep = random(800, 1500);
    console.log(
      `Loaded ${data.users.length} ${list}. Sleeping ${timeToSleep}ms to avoid rate limiting`,
    );

    await sleep(timeToSleep);

    return data.users.concat(
      await concatFriendshipsApiResponse(
        list,
        user_id,
        count,
        data.next_max_id,
      ),
    );
  }

  return data.users;
};

// helper methods to make the code a bit more readable
const getFollowers = (user_id, count = 50, next_max_id = "") => {
  return concatFriendshipsApiResponse("followers", user_id, count, next_max_id);
};

const getFollowing = (user_id, count = 50, next_max_id = "") => {
  return concatFriendshipsApiResponse("following", user_id, count, next_max_id);
};

const getUserId = async (username) => {
  let user = username;

  const lower = user.toLowerCase();
  const url = `https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query=${lower}&include_reel=false`;
  const data = await fetch(url, fetchOptions).then((r) => r.json());

  const result = data.users?.find(
    (result) => result.user.username.toLowerCase() === lower,
  );

  return result?.user?.pk || null;
};

const getUserFriendshipStats = async (username) => {
  const user_id = await getUserId(username);

  if (!user_id) {
    throw new Error(`Could not find user with username ${username}`);
  }

  const followers = await getFollowers(user_id);
  const following = await getFollowing(user_id);

  const followersUsernames = followers.map((follower) =>
    follower.username.toLowerCase(),
  );
  const followingUsernames = following.map((followed) =>
    followed.username.toLowerCase(),
  );

  const followerSet = new Set(followersUsernames);
  const followingSet = new Set(followingUsernames);

  console.log(Array(28).fill("-").join(""));
  console.log(
    `Fetched`,
    followerSet.size,
    "followers and ",
    followingSet.size,
    " following.",
  );

  console.log(
    `If this doesn't seem right then some of the output might be inaccurate`,
  );

  const PeopleIDontFollowBack = Array.from(followerSet).filter(
    (follower) => !followingSet.has(follower),
  );

  const PeopleNotFollowingMeBack = Array.from(followingSet).filter(
    (following) => !followerSet.has(following),
  );

  return {
    PeopleIDontFollowBack,
    PeopleNotFollowingMeBack,
  };
};


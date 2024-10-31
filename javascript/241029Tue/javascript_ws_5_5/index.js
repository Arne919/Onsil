// 이걸 어예하너...

// 버튼에 함수를 연결하기 위해 버튼 요소와 search-result 요소를 가져옵니다.
const searchInput = document.querySelector('.search-box__button');
const searchResult = document.querySelector('.search-result');

let page = 1;
let limit = 100;

// 버튼 클릭 시 fetchAlbums 함수를 실행하도록 이벤트를 추가합니다.
searchInput.addEventListener('click', fetchAlbums);

// 무한 스크롤을 위한 기준점을 설정하는 div를 생성합니다.
const sentinel = document.createElement('div');
sentinel.id = 'sentinel';
createObserver(sentinel); // IntersectionObserver를 설정합니다.

// axios 요청 전 로더를 표시하고, 요청 결과를 받아옵니다.
// HTML 생성은 별도 함수에서 처리합니다.
async function fetchAlbums(page = 1, limit = 100) {
  // 로딩 애니메이션 표시를 위해 로더 요소를 가져와 표시합니다.
  const loadingList = document.querySelector('.search-result--loadingList');
  loadingList.style.display = 'block';

  // 입력값이 없으면 함수를 종료합니다.
  const keyword = document.querySelector('.search-box__input').value;
  if (!keyword.trim()) return;

  // 입력값이 있으면 axios 요청을 보냅니다.
  const API_KEY = '8014fb3f52e7ad3c6450253848b29351';
  const BASE_URL = 'http://ws.audioscrobbler.com/2.0/';
  const searchUrl = `?method=album.search&format=json`;
  const params = {
    api_key: API_KEY,
    album: keyword,
    page: page,
    limit: limit,
  };

  const requestUrl = BASE_URL + searchUrl;
  const res = await axios.get(requestUrl, { params });

  // 요청으로 받은 앨범 목록을 변수에 저장합니다.
  const albums = res.data.results.albummatches.album;

  // 로더를 다시 숨깁니다.
  loadingList.style.display = 'none';

  // 앨범 정보를 사용하여 카드를 생성합니다.
  appendAlbumCards(albums);
}

// 요청 결과인 앨범 데이터를 받아 HTML 요소를 생성하고, sentinel 이동을 담당하는 함수입니다.
function appendAlbumCards(albums) {
  const cardList = document.createDocumentFragment(); // 성능 최적화를 위한 DocumentFragment 사용
  albums.forEach(album => {
    
    // 왼쪽의 이미지 태그 생성
    const cardImg = document.createElement('img');
    cardImg.src = album.image[1]['#text'];

    // 오른쪽의 텍스트 콘텐츠 생성
    const cardArtistName = document.createElement('h2');
    const cardAlbumName = document.createElement('p');
    cardArtistName.innerText = album.artist;
    cardAlbumName.innerText = album.name;

    // 텍스트 박스 생성
    const cardText = document.createElement('div');
    cardText.classList.add('search-result__text');
    cardText.append(cardArtistName, cardAlbumName);

    // 카드 생성 (왼쪽 이미지 + 오른쪽 텍스트)
    const card = document.createElement('div');
    card.classList.add('search-result__card');
    card.append(cardImg, cardText);

    // 카드 클릭 시 앨범 URL로 이동합니다.
    card.addEventListener('click', () => {
      window.location.href = album.url;
    });

    // 카드 리스트에 카드 요소 추가
    cardList.appendChild(card);
  });

  // 검색 결과 영역에 생성한 카드 리스트 추가
  searchResult.append(cardList);

  // 무한 스크롤용 sentinel 요소를 검색 결과 영역 아래로 이동합니다.
  searchResult.append(sentinel);
}

/* 
  ===== 
  무한 스크롤을 위한 IntersectionObserver 설정
  =====
*/
function createObserver(target) {
  const getMoreAlbums = (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        page += 1;
        fetchAlbums(page); // 다음 페이지의 앨범을 요청합니다.
      }
    });
  };

  const observer = new IntersectionObserver(getMoreAlbums);
  observer.observe(target); 
}

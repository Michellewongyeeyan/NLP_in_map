type TTPSidebar = {
    text? : string
    items : TTPSidebarItem[]
}

type TTPSidebarItem = {
    text: string
    link: string
    items?: TTTPSidebar[]
}

type TChapterMap = {
    chapter: number;
    location: string;
    nominatim: number[];
    lines: number[];
    count: number;
    text: string[];
    id: string;
}
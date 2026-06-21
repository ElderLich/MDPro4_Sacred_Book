-- senator.lua
-- Custom global utility file for Egyptian God card support

local god_mention_map = {
    [4059313] = {10000010},
    [10000040] = {10000000, 10000020, 10000010},
    [10000080] = {10000010},
    [10000090] = {10000010, 10000080},
    [11587414] = {10000010, 10000090},
    [12930501] = {10000010},
    [15771991] = {10000010},
    [22082432] = {10000010},
    [41044418] = {10000010},
    [42469671] = {10000020},
    [59094601] = {10000020},
    [74875003] = {10000000, 10000020, 10000010},
    [77432167] = {10000010},
    [78665705] = {10000010},
    [79339613] = {10000000},
    [79868386] = {10000000},
    [85182315] = {10000000},
    [85758066] = {10000000},
    [130000000] = {10000000, 10000020, 10000010},
    [130000001] = {10000000},
    [130000003] = {10000010, 10000080, 10000090},
    [130000004] = {10000020},
    [130000008] = {10000010},
    [130000010] = {10000020},
    [130000011] = {10000000, 10000020, 10000010},
    [130000014] = {10000000, 10000020, 10000010},
    [130000015] = {10000000, 10000020, 10000010},
}

-- Check if a card mentions a specific Egyptian God
function aux.MentionsCode(c,code)
    local list = god_mention_map[c:GetCode()]
    if not list then return false end
    for _,v in ipairs(list) do
        if v == code then return true end
    end
    return false
end

-- Check if a card mentions ANY Egyptian God
function aux.MentionsAnyGod(c)
    return aux.MentionsCode(c,10000000) -- Obelisk
        or aux.MentionsCode(c,10000010) -- Ra
        or aux.MentionsCode(c,10000020) -- Slifer
end

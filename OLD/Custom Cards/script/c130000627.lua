-- Number 199: Serket the Gluttonous
local s, id = GetID()
function s.initial_effect(c)
    -- Xyz summon
    aux.AddXyzProcedure(c, aux.FilterBoolFunction(Card.IsRace, RACE_ILLUSION), 5, 2)
    c:EnableReviveLimit()

    -- Attach monsters sent to opponent's GY as Xyz Material
    local e1 = Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_TO_GRAVE)
    e1:SetRange(LOCATION_MZONE)
    e1:SetCondition(s.attachcon)
    e1:SetOperation(s.attachop)
    c:RegisterEffect(e1)

    -- Optional destruction prevention by detaching 2 Xyz Materials
    local e2 = Effect.CreateEffect(c)
    e2:SetType(EFFECT_TYPE_CONTINUOUS + EFFECT_TYPE_SINGLE)
    e2:SetCode(EFFECT_DESTROY_REPLACE)
    e2:SetRange(LOCATION_MZONE)
    e2:SetTarget(s.reptg)
    e2:SetCountLimit(1,id)
    e2:SetOperation(s.repop)
    c:RegisterEffect(e2)

    -- Gain 200 ATK per Xyz Material
    local e3 = Effect.CreateEffect(c)
    e3:SetType(EFFECT_TYPE_SINGLE)
    e3:SetCode(EFFECT_UPDATE_ATTACK)
    e3:SetValue(s.atkval)
    c:RegisterEffect(e3)

    -- Return card from GY or banishment to Deck (Quick Effect)
    local e4 = Effect.CreateEffect(c)
    e4:SetDescription(aux.Stringid(id, 0))
    e4:SetCategory(CATEGORY_TODECK)
    e4:SetType(EFFECT_TYPE_QUICK_O)
    e4:SetCode(EVENT_FREE_CHAIN)
    e4:SetRange(LOCATION_MZONE)
    e4:SetHintTiming(0, TIMINGS_CHECK_MONSTER + TIMING_END_PHASE)
    e4:SetCountLimit(1, id)
    e4:SetCondition(s.quickcon)
    e4:SetTarget(s.tdtg)
    e4:SetOperation(s.tdop)
    c:RegisterEffect(e4)
end

-- Attach only monsters sent to opponent's GY
function s.attachfilter(c, tp)
    return c:IsLocation(LOCATION_GRAVE)
            and c:GetOwner() ~= tp
            and c:IsType(TYPE_MONSTER)
            and (not re or re:GetHandler() ~= e:GetHandler())
end
function s.attachcon(e, tp, eg, ep, ev, re, r, rp)
    return eg:IsExists(s.attachfilter, 1, nil, tp)
end
function s.attachop(e, tp, eg, ep, ev, re, r, rp)
    local c = e:GetHandler()
    local g = eg:Filter(s.attachfilter, nil, tp)
    for tc in aux.Next(g) do
        Duel.Overlay(c, tc)
    end
end

-- Optional destruction prevention
function s.reptg(e, tp, eg, ep, ev, re, r, rp, chk)
    local c = e:GetHandler()
    if chk == 0 then
        return eg:IsContains(c) and c:CheckRemoveOverlayCard(tp, 2, REASON_EFFECT)
    end
    if Duel.SelectYesNo(tp, aux.Stringid(id, 1)) then
        return true
    else
        return false
    end
end
function s.repop(e, tp, eg, ep, ev, re, r, rp)
    e:GetHandler():RemoveOverlayCard(tp, 2, 2, REASON_EFFECT)
end

-- Gain 300 ATK per Xyz Material
function s.atkval(e, c)
    return c:GetOverlayCount() * 200
end

-- Return card from GY or banishment to Deck
function s.tdfilter(c)
    return c:IsAbleToDeck()
end
function s.quickcon(e, tp, eg, ep, ev, re, r, rp)
    return Duel.GetTurnPlayer() ~= tp -- Only usable during the opponent's turn
end
function s.tdtg(e, tp, eg, ep, ev, re, r, rp, chk)
    if chk == 0 then
        return Duel.IsExistingMatchingCard(s.tdfilter, tp, LOCATION_GRAVE + LOCATION_REMOVED, LOCATION_GRAVE + LOCATION_REMOVED, 1, nil)
    end
    Duel.SetOperationInfo(0, CATEGORY_TODECK, nil, 1, 0, 0)
end
function s.tdop(e, tp, eg, ep, ev, re, r, rp)
    Duel.Hint(HINT_SELECTMSG, tp, HINTMSG_TODECK)
    local g = Duel.SelectMatchingCard(tp, s.tdfilter, tp, LOCATION_GRAVE + LOCATION_REMOVED, LOCATION_GRAVE + LOCATION_REMOVED, 1, 1, nil)
    if #g > 0 then
        Duel.SendtoDeck(g, nil, SEQ_DECKSHUFFLE, REASON_EFFECT)
    end
end

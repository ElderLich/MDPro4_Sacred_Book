--Foundation Slime
local s,id=GetID()

-- Divine-Beast mention map
local mentions = {
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
}

function s.initial_effect(c)
	-- Effect ①: Send Divine-Beast from Deck to GY and search
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOGRAVE+CATEGORY_SEARCH+CATEGORY_TOHAND)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetCode(EVENT_SUMMON_SUCCESS)
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCountLimit(1,id)
	e1:SetTarget(s.tg1)
	e1:SetOperation(s.op1)
	c:RegisterEffect(e1)
	local e2=e1:Clone()
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e2)

	-- Effect ②: Discard to increase Level by 6
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,1))
	e3:SetType(EFFECT_TYPE_IGNITION)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1,id+1)
	e3:SetCost(s.lvcost)
	e3:SetOperation(s.lvop)
	c:RegisterEffect(e3)
end

--========================
-- Effect ① Helpers
--========================

function s.tgfilter(c)
	return c:IsRace(RACE_DIVINE) and c:IsAbleToGrave()
end

function s.mentionsDivine(c,code)
	local list = mentions[c:GetCode()]
	if not list then return false end
	for _,v in ipairs(list) do
		if v == code then return true end
	end
	return false
end

function s.thfilter(c,code)
	return c:IsType(TYPE_SPELL+TYPE_TRAP)
		and c:IsAbleToHand()
		and s.mentionsDivine(c,code)
end

function s.tg1(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.tgfilter,tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOGRAVE,nil,1,tp,LOCATION_DECK)
end

function s.op1(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	local g=Duel.SelectMatchingCard(tp,s.tgfilter,tp,LOCATION_DECK,0,1,1,nil)
	local tc=g:GetFirst()
	if not tc then return end
	if Duel.SendtoGrave(tc,REASON_EFFECT)==0 or not tc:IsLocation(LOCATION_GRAVE) then return end
	local code=tc:GetOriginalCode()
	local sg=Duel.GetMatchingGroup(s.thfilter,tp,LOCATION_DECK,0,nil,code)
	if #sg>0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
		local sc=sg:Select(tp,1,1,nil):GetFirst()
		if sc then
			Duel.SendtoHand(sc,nil,REASON_EFFECT)
			Duel.ConfirmCards(1-tp,sc)
		end
	end
end

--========================
-- Effect ②: Discard to Gain Level
--========================

function s.lvcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,1,nil) end
	Duel.DiscardHand(tp,Card.IsDiscardable,1,1,REASON_COST+REASON_DISCARD)
end

function s.lvop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) or not c:IsFaceup() then return end
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_UPDATE_LEVEL)
	e1:SetValue(6)
	e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	c:RegisterEffect(e1)
end

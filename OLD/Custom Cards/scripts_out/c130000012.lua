--War of God
local s,id=GetID()

function s.initial_effect(c)
	-- Activate at Battle Phase Start
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_DRAW+CATEGORY_DAMAGE+CATEGORY_TOGRAVE)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetHintTiming(TIMING_BATTLE_START)
	e1:SetCountLimit(1,id+EFFECT_COUNT_CODE_OATH)
	e1:SetCondition(s.condition)
	e1:SetTarget(s.target)
	e1:SetOperation(s.activate)
	c:RegisterEffect(e1)
end

-- Must be activated at the start of Battle Phase
function s.condition(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetCurrentPhase() == PHASE_BATTLE_START
end

-- Filter: target 1 monster whose original attribute is DIVINE
function s.filter(c)
	return c:IsFaceup() and c:GetOriginalAttribute() == ATTRIBUTE_DIVINE
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsOnField() and s.filter(chkc) end
	if chk==0 then return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TARGET)
	Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
	local tc=Duel.GetFirstTarget()
	if not tc or not tc:IsRelateToEffect(e) then return end

	-- Restrict attack to only the targeted monster
	local e1=Effect.CreateEffect(e:GetHandler())
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_CANNOT_ATTACK)
	e1:SetTargetRange(LOCATION_MZONE,0)
	e1:SetTarget(function(e,c) return c~=tc end)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)

	-- Skip Main Phase 2
	local e2=Effect.CreateEffect(e:GetHandler())
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_SKIP_M2)
	e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e2:SetTargetRange(1,0)
	e2:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e2,tp)

	-- Prompt player to choose 1 effect
	local opt = Auxiliary.SelectFromOptions(tp,
		{true, aux.Stringid(id,0), 1}, -- Each player draws to 6
		{true, aux.Stringid(id,1), 2}, -- Inflict 4000 damage
		{Duel.IsExistingMatchingCard(aux.TRUE,tp,0,LOCATION_MZONE,1,nil), aux.Stringid(id,2), 3} -- Send opponent’s monsters
	)

	if opt == 1 then
		-- Each player draws until they have 6 cards
		local h1=Duel.GetFieldGroupCount(tp,LOCATION_HAND,0)
		local h2=Duel.GetFieldGroupCount(1-tp,LOCATION_HAND,0)
		if h1 < 6 then Duel.Draw(tp,6-h1,REASON_EFFECT) end
		if h2 < 6 then Duel.Draw(1-tp,6-h2,REASON_EFFECT) end
	elseif opt == 2 then
		-- Inflict 4000 damage
		Duel.Damage(1-tp,4000,REASON_EFFECT)
	elseif opt == 3 then
		-- Send all monsters on opponent's field to the GY
		local g=Duel.GetMatchingGroup(aux.TRUE,tp,0,LOCATION_MZONE,nil)
		Duel.SendtoGrave(g,REASON_EFFECT)
	end
end

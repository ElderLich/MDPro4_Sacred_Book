-- God of Apophis
local s, id = GetID()
function s.initial_effect(c)
	-- Enable the Fusion Monster's revive limit (prevents it from being Special Summoned except by its proper method)
	c:EnableReviveLimit()

	-- Define the Fusion Summoning condition:
	-- Requires 1 "Trap" Monster and 2 Continuous Traps as materials
	-- s.trap_monster_filter: Filters the "Trap" Monster required for Fusion
	-- s.continuous_trap_filter: Filters Continuous Traps for the remaining 2 materials
	-- The second argument (2) ensures that exactly 2 materials of the second type (Continuous Traps) are used
	aux.AddFusionProcFunFun(c, s.trap_monster_filter, s.continuous_trap_filter, 2, true)

	-- Define the Contact Fusion procedure:
	-- Allows Fusion Summoning by shuffling materials from the hand, field, GY, or banished zone into the Deck
	-- Card.IsAbleToDeckOrExtraAsCost: Ensures the materials are valid and can be shuffled back
	-- aux.tdcfop(c): Handles the operation of shuffling the materials back and performing the Fusion Summon
	aux.AddContactFusionProcedure(c, Card.IsAbleToDeckOrExtraAsCost,
			LOCATION_HAND + LOCATION_MZONE + LOCATION_GRAVE + LOCATION_REMOVED, 0, aux.tdcfop(c))

	-- Restricts how the card can be Special Summoned
	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_SINGLE)
	e0:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e0:SetCode(EFFECT_SPSUMMON_CONDITION)
	c:RegisterEffect(e0)

	-- ① Cannot be used as Fusion Material
	local e1 = Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_CANNOT_BE_FUSION_MATERIAL)
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
	e1:SetValue(1)
	c:RegisterEffect(e1)

	-- ② Protection for itself and "Trap" monsters
	local e2 = Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_INDESTRUCTABLE_EFFECT)
	e2:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
	e2:SetRange(LOCATION_MZONE)
	e2:SetTargetRange(LOCATION_MZONE, 0)
	e2:SetTarget(s.prottg)
	e2:SetValue(1)
	c:RegisterEffect(e2)

	-- Indestructibility in battle
	local e3 = e2:Clone()
	e3:SetCode(EFFECT_INDESTRUCTABLE_BATTLE)
	c:RegisterEffect(e3)

	-- ③ Change opponent's activated effect
	local e4 = Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id, 0))
	e4:SetType(EFFECT_TYPE_QUICK_O)
	e4:SetCode(EVENT_CHAINING)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCountLimit(1, id)
	e4:SetCondition(s.chcon)
	e4:SetCost(s.chcost)
	e4:SetTarget(s.chtg)
	e4:SetOperation(s.chop)
	c:RegisterEffect(e4)

	-- ④ Multi-attack
	local e5 = Effect.CreateEffect(c)
	e5:SetType(EFFECT_TYPE_SINGLE)
	e5:SetCode(EFFECT_EXTRA_ATTACK_MONSTER)
	e5:SetValue(s.atkval)
	c:RegisterEffect(e5)

	-- ⑤ Special Summon "Apophis" token
	local e6 = Effect.CreateEffect(c)
	e6:SetCategory(CATEGORY_SPECIAL_SUMMON + CATEGORY_TOKEN)
	e6:SetType(EFFECT_TYPE_IGNITION)
	e6:SetRange(LOCATION_MZONE)
	e6:SetCountLimit(1, id + 1)
	e6:SetTarget(s.sptg)
	e6:SetOperation(s.spop)
	c:RegisterEffect(e6)
end

-- Filter for Trap Monster
function s.trap_monster_filter(c)
	return c:IsType(TYPE_TRAP) and c:IsType(TYPE_MONSTER)
end

-- Filter for Continuous Trap
function s.continuous_trap_filter(c)
	return c:IsType(TYPE_TRAP) and c:IsType(TYPE_CONTINUOUS)
end

-- Protection target for indestructibility
function s.prottg(e, c)
	return c == e:GetHandler() or s.trap_monster_filter(c)
end

-- Condition for changing opponent's activated effect
function s.chcon(e, tp, eg, ep, ev, re, r, rp)
	return rp == 1 - tp and re:IsActivated()
end

-- Target for changing opponent's effect
function s.chcost(e, tp, eg, ep, ev, re, r, rp, chk)
	if chk==0 then return e:GetHandler():IsReleasable() end
	-- Duel.Release(e:GetHandler(),REASON_COST)
end

-- Filter for valid target for effect change (monsters in the opponent's hand, field, or deck)
function s.filter(c)
	return c:IsType(TYPE_TRAP) and c:IsType(TYPE_CONTINUOUS) and c:IsFaceupEx()
end

-- Target for effect change
function s.chtg(e, tp, eg, ep, ev, re, r, rp, chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.filter,rp,0,LOCATION_HAND+LOCATION_MZONE+LOCATION_DECK,1,e:GetHandler())
	end
end

-- Effect change operation
function s.chop(e, tp, eg, ep, ev, re, r, rp)
	local g=Group.CreateGroup()
	Duel.ChangeTargetCard(ev,g)
	Duel.ChangeChainOperation(ev,s.repop)
end

-- Replace operation (change the effect)
function s.repop(e, tp, eg, ep, ev, re, r, rp)
	Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_DESTROY)
	local g=Duel.SelectMatchingCard(1-tp,s.filter,tp,0,LOCATION_HAND+LOCATION_MZONE+LOCATION_DECK,1,1,nil)
	if g:GetCount()>0 then
		Duel.Destroy(g,REASON_EFFECT)
	end
end

-- Multi-attack value
function s.atkval(e, c)
	return Duel.GetMatchingGroupCount(Card.IsType, c:GetControler(), LOCATION_GRAVE, 0, nil, TYPE_CONTINUOUS + TYPE_TRAP)
end

-- Special Summon "Apophis" token
function s.sptg(e, tp, eg, ep, ev, re, r, rp, chk)
	if chk == 0 then
		-- Check if opponent has space in their Monster Zone and if the token can be summoned
		return Duel.GetLocationCount(1 - tp, LOCATION_MZONE) > 0 and
				Duel.IsPlayerCanSpecialSummonMonster(tp, id + 1, 0, TYPES_TOKEN, 2000, 2200, 6, RACE_REPTILE, ATTRIBUTE_EARTH)
	end
	Duel.SetOperationInfo(0, CATEGORY_TOKEN, nil, 1, 0, 0)
	Duel.SetOperationInfo(0, CATEGORY_SPECIAL_SUMMON, nil, 1, 0, 0)
end

function s.spop(e, tp, eg, ep, ev, re, r, rp)
	if Duel.GetLocationCount(1 - tp, LOCATION_MZONE) > 0 and
			Duel.IsPlayerCanSpecialSummonMonster(tp, id + 1, 0, TYPES_TOKEN, 2000, 2200, 6, RACE_REPTILE, ATTRIBUTE_EARTH) then
		-- Create and summon the token
		local token = Duel.CreateToken(tp, id + 1)
		Duel.SpecialSummon(token, 0, tp, 1 - tp, false, false, POS_FACEUP)
	else
		Duel.Hint(HINT_MESSAGE, tp, "Cannot summon token: check opponent's Monster Zone space.")
	end
end
